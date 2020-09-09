import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

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
    return render_template('add_ticket.html', call_types=mongo.db.call_type.find(), end_users=mongo.db.end_user.find())

@app.route('/insert_ticket', methods=['POST'])
def insert_ticket():
    tickets = mongo.db.tickets
    tickets.insert_one(request.form.to_dict())
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