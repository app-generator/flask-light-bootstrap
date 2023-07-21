

def init_Db():
    # Get the parent directory
    parent_directory = os.path.dirname(current_directory)
    envPath = parent_directory + '\.env'
    load_dotenv(envPath)
    dbCon = pymysql.connect(
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
            host=os.environ.get('IP_ADDRESS'),
            database=os.environ.get('DB_DATABASE')
     )
    
    # Connect to the database
    cursor = dbCon.cursor()

    return dbCon, cursor


def dbPerform(dbCon, cursor, action, inboundBool ):
    init_Db()
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
   