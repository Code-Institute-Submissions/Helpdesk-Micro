import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime

from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["MONGO_DBNAME"] = "HelpdeskDB"

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_tickets')
def get_tickets():
    tickets = mongo.db.tickets.find().sort('date_posted', -1)
    return render_template('tickets.html', tickets=tickets)

@app.route('/open_tickets')
def open_tickets():
    tickets = mongo.db.tickets.find({'call_status': 'Open'})
    return render_template('open_tickets.html', tickets=tickets)

@app.route('/held_tickets')
def held_tickets():
    tickets = mongo.db.tickets.find({'call_status': 'On Hold'})
    return render_template('held_tickets.html', tickets=tickets)

@app.route('/closed_tickets')
def closed_tickets():
    tickets = mongo.db.tickets.find({'call_status': 'Closed'})
    return render_template('closed_tickets.html', tickets=tickets)

@app.route('/add_ticket')
def add_ticket():
    eu_email = mongo.db.end_user.find()
    return render_template('add_ticket.html',   call_type=mongo.db.call_type.find(), 
                                                end_users=mongo.db.end_user.find(),
                                                call_priority=mongo.db.call_priority.find(),
                                                call_status=mongo.db.call_status.find(),
                                                eu_email=eu_email)
                                                


@app.route('/insert_ticket', methods=['POST', 'GET'])
def insert_ticket():
    tickets = mongo.db.tickets
    new_ticket =    {'date_posted': datetime.utcnow().strftime('%d %b %Y - %H:%M:%S'),
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

# increments the sequences mongoDB collection by one
def get_sequence(name):
    collection = mongo.db.sequences
    document = collection.find_one_and_update({"_id": name}, {"$inc": {"value": 1}}, return_document=True)

    return document["value"]

@app.route('/edit_ticket/<ticket_id>')
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

@app.route('/end_users')
def get_users():
    end_users = mongo.db.end_user.find().sort('end_user', 1)
    return render_template('end_users.html', end_users=end_users)

@app.route('/add_end_user')
def add_end_user():
    return render_template('add_end_user.html')

@app.route('/edit_end_user/<end_user_id>')
def edit_end_user(end_user_id):
    edit_end_user = mongo.db.end_user.find_one({"_id": ObjectId(end_user_id)})
    return render_template('edit_end_user.html', end_user=edit_end_user)

@app.route('/update_end_user/<end_user_id>', methods=["POST"])
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
def insert_end_user():
    end_user = mongo.db.end_user
    end_user.insert_one(request.form.to_dict())
    return redirect(url_for('get_users'))

@app.route('/delete_end_user/<end_user_id>')
def delete_end_user(end_user_id):
    mongo.db.end_user.remove({'_id': ObjectId(end_user_id)})
    return redirect(url_for('get_users'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)