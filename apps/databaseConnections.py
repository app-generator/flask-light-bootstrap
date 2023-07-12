import sqlite3

class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.LargeBinary)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)

def get_user_by_username(username):
    return Users.query.filter_by(username=username).first()

def get_post_by_title(title):
    return Posts.query.filter_by(title=title).first()

def start_stop_connections(dbAction, variable):
    # Connect to the SQLite database
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    ##
     
    dbAction(variable)
    # Closing the connection
    conn.close()



# Inserting data into the table
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('John Doe', 'john@example.com'))
conn.commit()

# Retrieving data from the table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Printing the retrieved data
for row in rows:
    print("ID:", row[0])
    print("Name:", row[1])
    print("Email:", row[2])
    print()


app = Flask(__name__)

# SQLite database connection
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

#inserting data into the emailFreeSubscribers table
@app.route('/', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        email = request.form['email']

        # Insert email into the SQLite database
        cursor.execute("INSERT INTO Subscribers (email) VALUES (?)", (email,))
        conn.commit()

        # You can add additional logic here, such as sending a confirmation email

        return "Thank you for subscribing!"

    return render_template('index.html')

if __name__ == '__main__': 
   app.run(debug=True)