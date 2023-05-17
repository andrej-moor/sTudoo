from flask import Flask, render_template, url_for, request, redirect, session
import sqlite3
from flask import flash


app = Flask(__name__)
app.secret_key = 'blablabla'
# secret key needed to encrypt data so it cannot be read in plaintext
# stronger key = more security
# without secret key --> runtime error, session is unavailable because no secret key was set

DB_NAME = 'users.db'

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    
    #cursor object can execute sql statements and get stored data from the database
    #cursor.execute is called and executes the following sql statement that creates a table, email must be unique
    
    
def insert_user(first_name, last_name, email, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)',
                   (first_name, last_name, email, password))
    conn.commit()
    conn.close()
    
    #placeholders = ?
    #insert into users: values stored in users.db with sql statement

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        insert_user(first_name, last_name, email, password)
        return redirect(url_for('signed_up'))

    return render_template('sign_up.html')

# POST: this block of code is only run when a form is submitted (in sign_up.html)
# sign_up has a form method POST that submits the user input
# call insert_user to store the user input to users.db
# redirect to signed_up when sign_up is successful
# otherwise show sign_up page to try again


@app.route("/signed_up")
def signed_up():
    return render_template("signed_up.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # code is only run when login form is submitted
        email = request.form['email']
        password = request.form['password']
        # receive data from request form

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        # sql statement to get user input (email, password) from database
        user = cursor.fetchone()
        conn.close()

        if user:
            session['user_id'] = user[0] 
            # Store user ID in the session, user id is stored in database
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        # User is logged in
        user_id = session['user_id']
        # is user id = session id
        return render_template('dashboard.html', user_id=user_id)
    else:
        flash('You must be logged in to access the dashboard.', 'error')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear() 
    # Clear session data
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    create_table()
    app.run(debug=True)