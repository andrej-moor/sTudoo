from flask import Blueprint, render_template, redirect, request, jsonify, session, url_for

from app.database import CLASSES_DB, delete_class, delete_project, delete_todo, insert_class, insert_project, insert_todo

import sqlite3

# ==== LISTS RELATED ROUTES ====

entries_bp = Blueprint('entries', __name__)

@entries_bp.route('/classes', methods=['GET', 'POST'])
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

    
    #return render_template('classes.html', title="Your Classes",
    #class_list=['Objektorientierte Programierung 1',
    #'Objektorientierte Programmierung 2','Datenbanken', 'Programmierung von Webapplikationen'])

@entries_bp.route('/projects', methods=['GET', 'POST'])
def projects():
    if 'user_id' in session:
        user_id = session['user_id']

        if request.method == 'POST':
            if 'add_project' in request.form:
                project_name = request.form.get('project_name')
                class_id = request.form.get('class_id')
                insert_project(user_id, class_id, project_name)

        # Retrieve the available classes from the database
        conn = sqlite3.connect(CLASSES_DB)
        cursor = conn.cursor()
        cursor.execute('SELECT class_id, name FROM classes WHERE user_id = ?', (user_id,))
        classes = cursor.fetchall()

        # Retrieve the available projects from the database
        cursor.execute('SELECT project_id, name FROM projects WHERE user_id = ?', (user_id,))
        projects = cursor.fetchall()

        conn.close()

        return render_template('projects.html', title="Your Projects", classes=classes, project_list=projects)


        #return render_template('projects.html', title="Your Projects", class_count=class_count, classes=classes, project_list=['Hausarbeit Grundlagen der WI',
    #'Präsentation Englisch 1','Android Todo App', 'Klausur Rechnungswesen'])

    # user_id is not in session, redirect to login site
   # return redirect(url_for('login'))

@entries_bp.route('/get_projects')
def get_projects():
    class_id = request.args.get('class_id')

    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('SELECT project_id, name FROM projects WHERE class_id = ?', (class_id,))
    projects = cursor.fetchall()
    conn.close()

    return jsonify(projects)

# had to research a lot because the select fields would not show the projects for the classes
# copied this from stackoverflow because I have very little knowledge about javascript/jsonify

@entries_bp.route('/todos', methods=['GET', 'POST'])
def todos():
    if 'user_id' in session:
        user_id = session['user_id']

        if request.method == 'POST':
            if 'add_todo' in request.form:
                todo_name = request.form.get('todo_name')
                class_id = request.form.get('class_id')
                project_id = request.form.get('project_id')
                insert_todo(user_id, class_id, project_id, todo_name)

        # Retrieve the available classes from the database
        conn = sqlite3.connect(CLASSES_DB)
        cursor = conn.cursor()
        cursor.execute('SELECT class_id, name FROM classes WHERE user_id = ?', (user_id,))
        classes = cursor.fetchall()

        # Retrieve the available projects for each class
        projects_by_class = {}
        for class_id, class_name in classes:
            cursor.execute('SELECT project_id, name FROM projects WHERE class_id = ? AND user_id = ?', (class_id, user_id))
            projects = cursor.fetchall()
            projects_by_class[class_id] = projects

        # Retrieve the todos from the database
        cursor.execute('SELECT todo_id, name FROM todos WHERE user_id = ?', (user_id,))
        todos = cursor.fetchall()

        conn.close()

        return render_template('todos.html', title="Your Todos", classes=classes, projects_by_class=projects_by_class, todo_list=todos)


    # user_id is not in session, redirect to login site
    return redirect(url_for('login'))


       # return render_template('todos.html', title="Your Todos", class_count=class_count, classes=classes, projects=projects, selected_class_id=request.form.get('class_id'), todo_list=['Recherche: Thema Hausarbeit',
    #'Outline für Präsentation','Brainstorming: Android App',' Lernplan Klausur Rechnungswesen'])
  
@entries_bp.route('/delete_entry', methods=['POST'])
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


