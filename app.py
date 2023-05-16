from flask import Flask, render_template, url_for, request, redirect, session
import sqlite3
from flask import flash


app = Flask(__name__)
app.secret_key = 'your_secret_key'
DB_NAME = 'users.db'
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()

def insert_user(first_name, last_name, email, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)',
                   (first_name, last_name, email, password))
    conn.commit()
    conn.close()

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
        return redirect(url_for('signed_up'))  # Redirect to the signed_up page

    return render_template('sign_up.html')   


@app.route("/signed_up")
def signed_up():
    return render_template("signed_up.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()

        if user:
            session['user_id'] = user[0]  # Store the user ID in the session
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        # User is logged in, retrieve user data or perform any required actions
        user_id = session['user_id']
        # Additional code to fetch user data from the database
        return render_template('dashboard.html', user_id=user_id)
    else:
        flash('You must be logged in to access the dashboard.', 'error')
        return redirect(url_for('login'))

    
    
@app.route('/logout')
def logout():
    session.clear()  # Clear the session data
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)