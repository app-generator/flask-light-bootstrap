import os
from dotenv import load_dotenv
import pymysql

def init_Db():
    # Get the parent directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    envPath = parent_directory + '\.env'
    load_dotenv(envPath)
    
    dbCon = pymysql.connect(
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
            host=os.environ.get('IP_ADDRESS'),
            database=os.environ.get('DB_NAME')
     )
    
    # Connect to the database
    cursor = dbCon.cursor()

    return dbCon, cursor


def dbPerform( action, isInboundBool ):
    dbCon, cursor = init_Db()
    try:
        if inboundBool: 
         # Execute the create table queries
         cursor.execute(action)
         print('Database manipulated successfully.')
        else: 
            retrievedInfo = cursor.execute(action)
            print('Database manipulated successfully.')

    except pymysql.connector.Error as err:
              print(f"Error editing {err}")
    finally:
           cursor.close()
           dbCon.close()
           print('succ')
    
    if not inboundBool: 
         
         return retrievedInfo
  
           


    

def dbActionInsertUser( name, password, email, billingDate, isPremium ):
    insertData = """ 
            
            INSERT INTO Customers (username, password, email, billingDate, activePremium,);
            VALUES ('{}','{}','{}','{}','{}');

    """.format( name, password, email, billingDate, isPremium )
    return insertData

def dbActionRetreiveUser( name, password, billingDate, isPremium ):
    data = """ 
            
            SELECT  FROM users 
            VALUES ('{}','{}','{}','{}');

    """.format( name, password, billingDate, isPremium )
    return data

def dbActionReturnNews():
   
    returnNews = """
    SELECT * WHERE {};
    
    
    """.format()
    print('return')
    return create_table_query
   