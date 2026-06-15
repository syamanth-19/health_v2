from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, jsonify
import os
from dotenv import load_dotenv
from models import db, mhusers  


load_dotenv()

mr = Blueprint("mr", __name__)

@mr.route('/login', methods = ['POST']) 
def login(): 
    return None 

@mr.route('/', methods = ['GET'])
def home():
    return jsonify({
        'route' : 'base page',
        'greetings' : 'welcome to MedhaIR Health solutions ! '
    }), 200
