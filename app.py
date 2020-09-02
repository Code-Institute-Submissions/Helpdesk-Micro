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
    tickets = list(mongo.db.tickets.find())
    return render_template('tickets.html', tickets=tickets)

@app.route('/add_ticket')
def add_ticket():
    return render_template('add_ticket.html', call_types=mongo.db.call_type.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)