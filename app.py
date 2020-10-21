import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["MONGO_DBNAME"] = "HelpdeskDB"
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

mongo = PyMongo(app)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        admin_user = mongo.db.admin_users.find_one(
            {"admin_username": request.form.get("admin_username").lower()})

        if admin_user:
            if check_password_hash(admin_user["admin_password"], request.form.get("admin_password")):
                session['logged_in'] = True
                return redirect(url_for('get_tickets'))
        else:
            error = 'invalid credentials'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/')
@login_required
def home():
    return redirect(url_for('get_tickets'))

@app.route('/get_tickets')
@login_required
def get_tickets():
    tickets = mongo.db.tickets.find().sort('date_posted', -1)
    return render_template('tickets.html', tickets=tickets)

@app.route('/open_tickets')
@login_required
def open_tickets():
    tickets = mongo.db.tickets.find({'call_status': 'Open'})
    return render_template('open_tickets.html', tickets=tickets)

@app.route('/held_tickets')
@login_required
def held_tickets():
    tickets = mongo.db.tickets.find({'call_status': 'On Hold'})
    return render_template('held_tickets.html', tickets=tickets)

@app.route('/closed_tickets')
@login_required
def closed_tickets():
    tickets = mongo.db.tickets.find({'call_status': 'Closed'})
    return render_template('closed_tickets.html', tickets=tickets)

@app.route('/tickets/<ticket_id>')
def ticket_full_detail(ticket_id):
    ticket = mongo.db.tickets.find_one({'_id': ObjectId(ticket_id)})
    updates = mongo.db.ticket_updates.find({'ticket_id': str(ticket_id)})
    return render_template('full_ticket.html', ticket=ticket, updates=updates)

@app.route('/add_ticket')
@login_required
def add_ticket():
    eu_email = mongo.db.end_user.find()
    return render_template('add_ticket.html',   call_type=mongo.db.call_type.find(), 
                                                end_users=mongo.db.end_user.find(),
                                                call_priority=mongo.db.call_priority.find(),
                                                call_status=mongo.db.call_status.find(),
                                                eu_email=eu_email)
                                                


@app.route('/insert_ticket', methods=['POST', 'GET'])
@login_required
def insert_ticket():
    tickets = mongo.db.tickets
    new_ticket =    {'date_posted': datetime.utcnow().strftime('%d/%m/%y @ %H:%M:%S'),
                    'call_subject': request.form.get('call_subject'),
                    'call_details': request.form.get('call_details'),
                    'call_type': request.form.get('call_type'),
                    'call_priority': request.form.get('call_priority'),
                    'call_status': request.form.get('call_status'),
                    'end_user': request.form.get('end_user'),
                    'eu_email': request.form.get('eu_email'),
                    "_ticketid": get_sequence("messages"), # inserts the incremented ticketid from get_sequence function
                    }
                    
    tickets.insert_one((new_ticket))
    return redirect(url_for('get_tickets'))

# increments the sequences mongoDB collection by one on each add_ticket call
def get_sequence(name):
    collection = mongo.db.sequences
    document = collection.find_one_and_update({"_id": name}, {"$inc": {"value": 1}}, return_document=True)

    return document["value"]

@app.route('/edit_ticket/<ticket_id>')
@login_required
def edit_ticket(ticket_id):
    edit_ticket = mongo.db.tickets.find_one({"_id": ObjectId(ticket_id)})
    end_user = mongo.db.end_user.find()
    call_type = mongo.db.call_type.find()
    call_priority = mongo.db.call_priority.find()
    call_status = mongo.db.call_status.find()
    eu_email = mongo.db.eu_email.find()
    return render_template('edit_ticket.html', ticket=edit_ticket,
                                               end_user=end_user,
                                               call_type=call_type,
                                               call_priority=call_priority,
                                               call_status=call_status,
                                               eu_email=eu_email)

@app.route('/update_ticket/<ticket_id>', methods=['POST', 'GET'])
@login_required
def update_ticket(ticket_id):
    tickets = mongo.db.tickets
    tickets.update({'_id': ObjectId(ticket_id)},
    {
        'call_subject':request.form.get('call_subject'),
        'call_details':request.form.get('call_details'),
        'call_type':request.form.get('call_type'),
        'call_priority':request.form.get('call_priority'),
        'call_status':request.form.get('call_status'),
        'end_user':request.form.get('end_user'),
        'eu_email':request.form.get('eu_email'),
        '_ticketid':request.form.get('_ticketid'),
        'date_posted':request.form.get('date_posted')
    })
    return redirect(url_for('get_tickets'))

@app.route('/get_tickets/add_quick_update', methods=['GET', 'POST'])
def new_update():
    updates = mongo.db.ticket_updates
    update = {
        'date_posted': datetime.utcnow().strftime('%d/%m/%y @ %H:%M:%S'),
        'add_update': request.form.get('add_update'),
        'ticket_id': request.form.get('ticket_id'),
    }
    updates.insert_one(update)
    return redirect(url_for('get_tickets', ticket_id=request.form.get('ticket_id')))

@app.route('/open_tickets/add_quick_update_open', methods=['GET', 'POST'])
def new_update_open():
    updates = mongo.db.ticket_updates
    update = {
        'date_posted': datetime.utcnow().strftime('%d/%m/%y @ %H:%M:%S'),
        'add_update': request.form.get('add_update'),
        'ticket_id': request.form.get('ticket_id'),
    }
    updates.insert_one(update)
    return redirect(url_for('open_tickets', ticket_id=request.form.get('ticket_id')))

@app.route('/held_tickets/add_quick_update_hold', methods=['GET', 'POST'])
def new_update_hold():
    updates = mongo.db.ticket_updates
    update = {
        'date_posted': datetime.utcnow().strftime('%d/%m/%y @ %H:%M:%S'),
        'add_update': request.form.get('add_update'),
        'ticket_id': request.form.get('ticket_id'),
    }
    updates.insert_one(update)
    return redirect(url_for('held_tickets', ticket_id=request.form.get('ticket_id')))

@app.route('/closed_tickets/add_quick_update_closed', methods=['GET', 'POST'])
def new_update_closed():
    updates = mongo.db.ticket_updates
    update = {
        'date_posted': datetime.utcnow().strftime('%d/%m/%y @ %H:%M:%S'),
        'add_update': request.form.get('add_update'),
        'ticket_id': request.form.get('ticket_id'),
    }
    updates.insert_one(update)
    return redirect(url_for('closed_tickets', ticket_id=request.form.get('ticket_id')))

@app.route('/end_users')
@login_required
def get_users():
    end_users = mongo.db.end_user.find().sort('end_user', 1)
    return render_template('end_users.html', end_users=end_users)

@app.route('/add_end_user')
@login_required
def add_end_user():
    return render_template('add_end_user.html')

@app.route('/edit_end_user/<end_user_id>')
@login_required
def edit_end_user(end_user_id):
    edit_end_user = mongo.db.end_user.find_one({"_id": ObjectId(end_user_id)})
    return render_template('edit_end_user.html', end_user=edit_end_user)

@app.route('/update_end_user/<end_user_id>', methods=["POST"])
@login_required
def update_end_user(end_user_id):
    end_user = mongo.db.end_user
    end_user.update( {'_id': ObjectId(end_user_id)},
    {
        'end_user':request.form.get('end_user'),
        'tel_no':request.form.get('tel_no'),
        'eu_email':request.form.get('eu_email'),
        'eu_department':request.form.get('eu_department'),
    })
    return redirect(url_for('get_users'))

@app.route('/insert_end_user', methods=['POST'])
@login_required
def insert_end_user():
    end_user = mongo.db.end_user
    end_user.insert_one(request.form.to_dict())
    return redirect(url_for('get_users'))

@app.route('/delete_end_user/<end_user_id>')
@login_required
def delete_end_user(end_user_id):
    mongo.db.end_user.remove({'_id': ObjectId(end_user_id)})
    return redirect(url_for('get_users'))

@app.route('/admin_users')
@login_required
def get_admin_users():
    admin_users = mongo.db.admin_users.find().sort('admin_username', 1)
    return render_template('admin_users.html', admin_users=admin_users)

@app.route('/add_admin_user')
@login_required
def add_admin_user():
    return render_template('add_admin_user.html')

@app.route('/edit_admin_user/<admin_user_id>')
@login_required
def edit_admin_user(admin_user_id):
    edit_admin_user = mongo.db.admin_users.find_one({'_id': ObjectId(admin_user_id)})
    return render_template('edit_admin_user.html', admin_user=edit_admin_user)

@app.route('/update_admin_user/<admin_user_id>', methods=["POST", "GET"])
@login_required
def update_admin_user(admin_user_id):
    admin_user = mongo.db.admin_users
    admin_user.update({'_id': ObjectId(admin_user_id)},
    {
        'admin_username':request.form.get('admin_username'),
        "admin_password": generate_password_hash(request.form.get("admin_password"))
    })
    return redirect(url_for('get_admin_users'))

@app.route('/insert_admin_user', methods=['POST'])
@login_required
def insert_admin_user():
    new_admin = {
            "admin_username": request.form.get("admin_username"),
            "admin_password": generate_password_hash(request.form.get("admin_password"))}
    mongo.db.admin_users.insert_one(new_admin)
    return redirect(url_for('get_admin_users'))

@app.route('/delete_admin_user/<admin_user_id>')
@login_required
def delete_admin_user(admin_user_id):
    mongo.db.admin_users.remove({'_id': ObjectId(admin_user_id)})
    return redirect(url_for('get_admin_users'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)