import sqlite3

# ==== CREATE TABLES ====
CLASSES_DB = 'classes.db'

def create_users_table():
    conn = sqlite3.connect(CLASSES_DB)
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
    
   #cursor object can execute sql statements and get stored data from the database
   #cursor.execute is called and executes the following sql statement that creates a table, email must be unique
    
def create_classes_table():
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS classes (
            class_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()

def create_projects_table():
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            project_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            class_id INTEGER,
            name TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (class_id) REFERENCES classes (class_id)
        )
    ''')
    conn.commit()
    conn.close()
    #create projects table with foreign key referencing to user, so the projects
    #are created for the logged-in user
    #create classes table
    
def create_todos_table():
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            todo_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            class_id INTEGER,
            project_id INTEGER,
            name TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (class_id) REFERENCES classes (class_id),
            FOREIGN KEY (project_id) REFERENCES projects (project_id)
        )
    ''')
    conn.commit()
    conn.close()

    
   

# ==== USER ACCOUNT RELATED ====
def insert_user(first_name, last_name, email, password):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)',
                   (first_name, last_name, email, password))
    conn.commit()
    conn.close()
    
    #placeholders = ?
    #insert into users: values stored in classes.db with sql statement
    
def authenticate_user(email, password):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    conn.close()

    if user and user[4] == password:
        return True

    return False
   
def get_first_name(user_id):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('SELECT first_name FROM users WHERE id = ?', (user_id,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        return None
    
    #function to show first name on welcome page e.g. "Hey [first_name]"
    # result [0] = 1. Eintrag = first_name
 
def delete_user(email, password):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    
    if user and user[4] == password:
    # user [4] vergleicht, ob user und passwort (5. Spalte) miteinander übereinstimmen    
        
        #Delete user's projects
        cursor.execute('DELETE FROM projects WHERE user_id = ?', (user[0],))
        
        #Delete user's classes
        cursor.execute('DELETE FROM classes WHERE user_id = ?', (user[0],))
        
        #Delete user's todos
        cursor.execute('DELETE FROM todos WHERE user_id = ?', (user[0],))
        
        #Delete user
        cursor.execute('DELETE FROM users WHERE email = ?', (email,))
        
        conn.commit()
        conn.close()
        return True
    
    conn.close()
    return False

#projects/classes/to-dos functionality, add and delete

def insert_class(user_id, name):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()

    cursor.execute('INSERT INTO classes (user_id, name) VALUES (?, ?)', (user_id, name))
    # class_id = cursor.lastrowid
    conn.commit()
    conn.close()
    # return class_id
    return False

def insert_project(user_id, class_id, name):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()

    # class und user_id vorhanden?
    cursor.execute('SELECT class_id FROM classes WHERE class_id = ? AND user_id = ?', (class_id, user_id))
    class_exists = cursor.fetchone()
    # cursor fetchone ruft ab, ob bereits eine class in der datenbank angelegt ist
    # falls nicht wird False zurück gegeben (Z. 173)

    if class_exists:
        cursor.execute('INSERT INTO projects (user_id, class_id, name) VALUES (?, ?, ?)', (user_id, class_id, name))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False

def insert_todo(user_id, class_id, project_id, name):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()

    
    cursor.execute('SELECT class_id FROM classes WHERE class_id = ? AND user_id = ?', (class_id, user_id))
    class_exists = cursor.fetchone()
    # siehe insert project

    cursor.execute('SELECT project_id FROM projects WHERE project_id = ? AND class_id = ?', (project_id, class_id))
    project_exists = cursor.fetchone()
    # fetchone überprüft, ob bereits ein project angelegt ist
    # falls nicht wird False zurückgegeben (Z. 197)

    if class_exists and project_exists:
        cursor.execute('INSERT INTO todos (user_id, class_id, project_id, name) VALUES (?, ?, ?, ?)',
                       (user_id, class_id, project_id, name))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False

def delete_project(project_id):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM projects WHERE project_id = ?', (project_id,))
    cursor.execute('DELETE FROM todos WHERE project_id = ?' , (project_id,))
    # löscht die todos mit abhängigkeit zu projects
    conn.commit()
    conn.close()

def delete_class(class_id):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    
    # Löschen der Klasse
    cursor.execute('DELETE FROM classes WHERE class_id = ?', (class_id,))
    
    # Löschen der zugehörigen Projekte
    cursor.execute('DELETE FROM projects WHERE class_id = ?', (class_id,))
    
    # Löschen der zugehörigen Todos
    cursor.execute('DELETE FROM todos WHERE class_id = ?', (class_id,))
    
    conn.commit()
    conn.close()

def delete_todo(todo_id):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM todos WHERE todo_id = ?', (todo_id,))
    conn.commit()
    conn.close()


