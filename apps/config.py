# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""


from dotenv import load_dotenv
import os

class Config(object):


  
    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Get the parent directory
    parent_directory = os.path.dirname(current_directory)
    envPath = parent_directory + '\.env'
    load_dotenv(envPath)
  

    # Set up the App SECRET_KEY
    SECRET_KEY = os.getenv('SECRET_KEY')
    # outside docker
    #SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    #inside docker
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('IP_ADDRESS')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    

    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')    
    
class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

     # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        os.getenv('DB_ENGINE'  ),
        os.getenv('DB_USERNAME'),
        os.getenv('DB_PASS'    ),
        os.getenv('DB_HOST'     ),
        os.getenv('DB_PORT'   ),
        os.getenv('DB_NAME'    )
        )

class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}
