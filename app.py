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
    tickets = mongo.db.tickets.find()
    # end_user = list(mongo.db.end_user.find_one())
    return render_template('tickets.html', tickets=tickets)

@app.route('/add_ticket')
def add_ticket():
    return render_template('add_ticket.html',   call_type=mongo.db.call_type.find(), 
                                                end_users=mongo.db.end_user.find(),
                                                call_priority=mongo.db.call_priority.find(),
                                                call_status=mongo.db.call_status.find())

@app.route('/insert_ticket', methods=['POST'])
def insert_ticket():
    tickets = mongo.db.tickets
    new_ticket =    {'date_posted': datetime.utcnow(),
                    'call_subject': request.form.get('call_subject'),
                    'call_details': request.form.get('call_details'),
                    'call_type': request.form.get('call_type'),
                    'call_priority': request.form.get('call_priority'),
                    'call_status': request.form.get('call_status'),
                    'end_user': request.form.get('end_user')}
                    
    tickets.insert_one((new_ticket))
    return redirect(url_for('get_tickets'))

@app.route('/edit_ticket/<ticket_id>')
def edit_ticket(ticket_id):
    edit_ticket = mongo.db.tickets.find_one({"_id": ObjectId(ticket_id)})
    end_user = mongo.db.end_user.find()
    call_type = mongo.db.call_type.find()
    call_priority = mongo.db.call_priority.find()
    call_status = mongo.db.call_status.find()
    return render_template('edit_ticket.html', ticket=edit_ticket,
                                               end_user=end_user,
                                               call_type=call_type,
                                               call_priority=call_priority,
                                               call_status=call_status,)

@app.route('/update_ticket/<ticket_id>', methods=["POST"])
def update_ticket(ticket_id):
    tickets = mongo.db.tickets
    tickets.update( {'_id': ObjectId(ticket_id)},
    {
        'call_subject':request.form.get('call_subject'),
        'call_details':request.form.get('call_details'),
        'call_type':request.form.get('call_type'),
        'call_priority':request.form.get('call_priority'),
        'call_status':request.form.get('call_status'),
        'end_user':request.form.get('end_user')
    })
    return redirect(url_for('get_tickets'))

@app.route('/add_end_user')
def add_end_user():
    return render_template('add_end_user.html')

@app.route('/insert_end_user', methods=['POST'])
def insert_end_user():
    end_user = mongo.db.end_user
    end_user.insert_one(request.form.to_dict())
    return redirect(url_for('get_tickets'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)