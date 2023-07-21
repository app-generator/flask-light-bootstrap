# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from mysql.connector import errorcode
from logging import root
from flask import Flask
from flask_login import LoginManager
#from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from importlib import import_module
from dotenv import load_dotenv
from apps import config_db 
import os

from sqlalchemy import insert

 # Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

    # Get the parent directory
parent_directory = os.path.dirname(current_directory)
envPath = parent_directory + '\.env'
load_dotenv(envPath)

path = os.environ.get('IP_ADDRESS')
print('try start')
try:
    db = mysql.connector.connect(user='root', password='snooki1Kush4Cush' ,host='172.18.0.2', database='data_news')
    print('did try')

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  print('close')
  db.close()

print('try login ')
login_manager = LoginManager()


def register_extensions(app):
    
    login_manager.init_app(app)


def register_blueprints(app):
    for module_name in ('authentication', 'home'):
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def init_Db():

     # Connect to the database
     db = mysql.connector.connect(user='root', password='snooki1Kush4Cush', host='172.18.0.2', database='data_news')
     cursor = db.cursor()

     return db, cursor


def dbPerform(db, cursor, action, inboundBool ):
    try:
        if inboundBool: 
         # Execute the create table queries
         cursor.execute(action)
         print('Database manipulated successfully.')
        else: 
            retrieveInfo = cursor.execute(action)
            print('Database manipulated successfully.')

    except mysql.connector.Error as err:
              print(f"Error editing {err}")
    finally:
           cursor.close()
           db.close()
           print('succ')
    
    if not inboundBool: 
         
         return retrieveInfo
  
           


    
def dbActionCreateTable():
    # SQL queries to create the necessary tables
    # Adjust the queries according to your application's schema
    create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(20) NOT NULL,
            password VARCHAR(30) NOT NULL,
            email VARCHAR(40) NOT NULL, 
            activePremium BOOL,
            BillingDate DATE

        );
        
        CREATE TABLE IF NOT EXISTS newsArticles (
            id INT AUTO_INCREMENT PRIMARY KEY,
            category	TEXT,
            date	DATETIME,
            title	TEXT,
            topic	TEXT,
             content	TEXT,
            sentiment	DECIMAL,
            likes	INTEGER,
            comments	INTEGER,
            shares	INTEGER,
            keywords	TEXT,
            hashtags	TEXT,
            source_url	TEXT,
            tags	TEXT,
            ctr	REAL,
            spent	INTEGER,
            bounce_rate	REAL,
            location_name	TEXT
        );
          
       
       
    """
    return create_table_query
    print('succ')

def dbActionInsertUser(tableName, db, name, password, email, billingDate, isPremium ):
    insertData = """ 
            
            INSERT INTO Customers (username, password, email, billingDate, activePremium,);
            VALUES ('{}','{}','{}','{}','{}');

    """.format( name, password, email, billingDate, isPremium )
    return insertData

def dbActionRetreiveUser(tableName, db, name, password, email, billingDate, isPremium ):
    data = """ 
            
            SELECT  FROM users 
            VALUES ('{}','{}','{}','{}','{}');

    """.format( name, password, email, billingDate, isPremium )
    return data

def dbActionReturnNews():
   
    returnNews = """
    SELECT * WHERE {};
    
    
    """.format()
    print('return')
    return create_table_query
   

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    
    return app
