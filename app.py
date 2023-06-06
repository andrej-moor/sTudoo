from flask import Flask, render_template, url_for, request, redirect, session
import sqlite3
from flask import flash
from datetime import timedelta
from database import DB_NAME, create_table, insert_user, delete_account


app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)
app.secret_key = 'blablabla'
# secret key needed to encrypt data so it cannot be read in plaintext
# stronger key = more security
# without secret key --> runtime error, session is unavailable because no secret key was set


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
            session.permanent = True
            # Store user ID in the session, user id is stored in database
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('logedin'))
        else:
            flash('Invalid credentials. Please try again.', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logedin')
def logedin():
    if 'user_id' in session:
        # User is logged in
        user_id = session['user_id']
        # is user id = session id
        return render_template('logedin.html', user_id=user_id)
    else:
        return redirect(url_for('login'))
    
@app.route('/useraccount')
def useraccount():
    return render_template('user_account.html')

@app.route('/logout')
def logout():
    session.clear() 
    # Clear session data
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))


@app.route('/delete_account', methods=['POST'])
def delete_account():
    email = request.form['email']
    password = request.form['password']
    
    if delete_account(email, password):
        return redirect(url_for('index'), 'Account erfolgreich gelöscht')
    
    else:
        return 'Falsches Passwort'




if __name__ == '__main__':
    create_table()
    app.run(debug=True)