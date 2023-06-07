from flask import Flask, render_template, url_for, request, redirect, session
import sqlite3
from flask import flash
from datetime import timedelta
from database import (
    USERS_DB,
    create_table,
    insert_user,
    delete_user,
    get_first_name,
)
from database import (
    CLASSES_DB,
    create_classes_table,
    create_projects_table,
    create_todos_table,
    insert_class,
    insert_project,
    insert_todo,
    delete_class,
    delete_project,
    delete_todo  
)


app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)
app.secret_key = 'blablabla'
# secret key needed to encrypt data so it cannot be read in plaintext
# stronger key = more security
# without secret key --> runtime error, session is unavailable because no secret key was set

create_table()
create_classes_table()
create_projects_table()
create_todos_table()


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

        conn = sqlite3.connect(CLASSES_DB)
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

@app.route('/logedin', methods=['GET', 'POST'])
def logedin():
    if 'user_id' in session:
        user_id = session['user_id']
        first_name = get_first_name(user_id)
        
        if request.method == 'POST':
            print(request.form)  # debugging because the post is not getting the values from the form
            if 'add_project' in request.form:
                project_name = request.form['project_name']
                insert_project(user_id, project_name)
            elif 'add_class' in request.form:
                class_name = request.form['class_name']
                insert_class(user_id, class_name)
            elif 'add_todo' in request.form:
                todo_name = request.form['todo_name']
                insert_todo(user_id, todo_name)

        return render_template('logedin.html', user_id=user_id, first_name=first_name)
    else:
        return redirect(url_for('login'))

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/classes')
def classes():
    return render_template('classes.html')

@app.route('/todos')
def todos():
    return render_template('todos.html')
    
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
    
    if delete_user(email, password):
        return redirect(url_for('index'))

    return 'Incorrect email or password'



if __name__ == '__main__':
    create_table()
    app.run(debug=True)