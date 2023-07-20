from flask import Flask
app = Flask(__name__)

from flask import jsonify, render_template, url_for, request, redirect, session, flash

import sqlite3

from datetime import timedelta

from database import (
    CLASSES_DB,
    create_users_table,
    create_classes_table,
    create_projects_table,
    create_todos_table,
    insert_user,
    insert_class,
    insert_project,
    insert_todo,
    delete_user,
    delete_class,
    delete_project,
    delete_todo,
    get_first_name
)

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)
app.secret_key = 'blablabla'
# secret key needed to encrypt data so it cannot be read in plaintext
# stronger key = more security
# without secret key --> runtime error, session is unavailable because no secret key was set

create_users_table()
create_classes_table()
create_projects_table()
create_todos_table()


# ==== HOME, IMPRINT, PRIVACY ==== 
@app.route("/")
def index():
    return render_template('index.html', title="Home")

@app.route('/imprint')
def imprint():
    return render_template('imprint.html', title="Imprint")

@app.route('/privacy')
def privacy():
    return render_template('privacy.html', title="Privacy")

# ==== USER RELATED ROUTES ====

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        insert_user(first_name, last_name, email, password)
        return redirect(url_for('signed_up'))
    return render_template('sign_up.html', title="Sign-Up")

    # POST: this block of code is only run when a form is submitted (in sign_up.html)
    # sign_up has a form method POST that submits the user input
    # call insert_user to store the user input to classes.db
    # redirect to signed_up when sign_up is successful
    # otherwise show sign_up page to try again

@app.route("/signed_up")
def signed_up():
    return render_template("signed_up.html", title="You're Signed Up")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # dieser code wird nur ausgeführt, wenn eine post methode getriggert wird (anmeldeformular abschicken)
        email = request.form['email']
        password = request.form['password']
        # daten aus dem request form empfangen
        conn = sqlite3.connect(CLASSES_DB)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        # sql abfrage nach email und passwort
        user = cursor.fetchone()
        conn.close()

        if user:
            session['user_id'] = user[0] 
            session.permanent = True
            # user id in session speichern
            return redirect(url_for('logedin'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html', title="Login")

@app.route('/logedin', methods=['GET', 'POST'])
def logedin():
    if 'user_id' in session:
        user_id = session['user_id']
        first_name = get_first_name(user_id)
        return render_template('logedin.html', title="You're Loged in", user_id=user_id, first_name=first_name)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear() 
    # Clear session data
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@app.route('/useraccount')
def useraccount():
    return render_template('user_account.html', title="You're User Account")

@app.route('/delete_account', methods=['POST'])
def delete_account():
    email = request.form['email']
    password = request.form['password']
    if delete_user(email, password):
        return render_template('user_account_deleted.html', title="Account Deleted")
    return 'Incorrect email or password'

@app.route('/delete_site')
def delete_site():
    return render_template('user_account_delete.html', title="Delete Account")

# ==== LISTS RELATED ROUTES ====

@app.route('/classes', methods=['GET', 'POST'])
def classes():
    if 'user_id' in session:
        user_id = session['user_id']
    
    if request.method == 'POST':
        if 'add_class' in request.form:
            class_name = request.form.get('class_name')
            insert_class(user_id, class_name)
    
    # Daten aus der Datenbank abrufen
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('SELECT class_id, name FROM classes WHERE user_id = ?', (user_id,))
    class_list = cursor.fetchall()
    conn.close()

    return render_template('classes.html', title="Your Classes", class_list=class_list)


@app.route('/projects', methods=['GET', 'POST'])
def projects():
    if 'user_id' in session:
        user_id = session['user_id']
        if request.method == 'POST':
            if 'add_project' in request.form:
                project_name = request.form.get('project_name')
                class_id = request.form.get('class_id')
                insert_project(user_id, class_id, project_name)
                
        
        conn = sqlite3.connect(CLASSES_DB)
        cursor = conn.cursor()
        cursor.execute('SELECT class_id, name FROM classes WHERE user_id = ?', (user_id,))
        classes = cursor.fetchall()
        # alle verfügbaren classes des users im dropdown anzeigen
        cursor.execute('SELECT project_id, name FROM projects WHERE user_id = ?', (user_id,))
        projects = cursor.fetchall()
        # alle projects direkt nach dem hinzufügen anzeigen
        conn.close()
        return render_template('projects.html', title="Your Projects", classes=classes, project_list=projects)


@app.route('/get_projects')
def get_projects():
    class_id = request.args.get('class_id')

    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('SELECT project_id, name FROM projects WHERE class_id = ?', (class_id,))
    projects = cursor.fetchall()
    conn.close()
    return jsonify(projects)

    # had to research a lot because the select fields would not show the projects for the classes

@app.route('/todos', methods=['GET', 'POST'])
def todos():
    if 'user_id' in session:
        user_id = session['user_id']
        if request.method == 'POST':
            if 'add_todo' in request.form:
                todo_name = request.form.get('todo_name')
                class_id = request.form.get('class_id')
                project_id = request.form.get('project_id')
                insert_todo(user_id, class_id, project_id, todo_name)
                
        conn = sqlite3.connect(CLASSES_DB)
        cursor = conn.cursor()
        cursor.execute('SELECT class_id, name FROM classes WHERE user_id = ?', (user_id,))
        classes = cursor.fetchall()
        # alle verfügbaren classes für den user anzeigen (im dropdown)
        projects_by_class = {}
        # ich lege ein python dictionary an, das die einzelnen projekte mit der dazugehörigen
        # class_id verknüpft, sodass nur die projects einer class angezeigt werden
        # zb alle projects mit foreign key class_id = 1 werden angezeigt
        for class_id, class_name in classes:
            cursor.execute('SELECT project_id, name FROM projects WHERE class_id = ? AND user_id = ?', (class_id, user_id))
            projects = cursor.fetchall()
            projects_by_class[class_id] = projects
            # wähle für jede class_id und name das oder mehrere dazugehörige projects aus
            # speichere sie im dictionary 
        cursor.execute('SELECT todo_id, name FROM todos WHERE user_id = ?', (user_id,))
        todos = cursor.fetchall()
        conn.close()
        return render_template('todos.html', title="Your Todos", classes=classes, projects_by_class=projects_by_class, todo_list=todos)

    return redirect(url_for('login'))
    # falls user nicht mehr eingeloggt ist, redirect zu login page


@app.route('/delete_entry', methods=['POST'])
def delete_entry():
    entry_id = request.form.get('entry_id')
    entry_type = request.form.get('entry_type')
    
    if entry_type == 'class':
        delete_class(entry_id)
    elif entry_type == 'project':
        delete_project(entry_id)
    elif entry_type == 'todo':
        delete_todo(entry_id)
    else:
        return 'Error: Invalid entry type'
    return redirect(request.referrer)

if __name__ == '__main__':
    create_users_table()
    app.run(debug=True)