# store in separate class file for organizational purposes and clean code

import sqlite3

USERS_DB = 'users.db'
CLASSES_DB = 'classes.db'

#create user table
def create_table():
    conn = sqlite3.connect(USERS_DB)
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
    
    #create projects table with foreign key referencing to user, so the projects
    #are created for the logged-in user
    #create classes table
    
def create_classes_table():
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS classes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()

# create projects table
def create_projects_table():
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()

# create todos table
def create_todos_table():
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()
    
    #cursor object can execute sql statements and get stored data from the database
    #cursor.execute is called and executes the following sql statement that creates a table, email must be unique
    
    
def insert_user(first_name, last_name, email, password):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)',
                   (first_name, last_name, email, password))
    conn.commit()
    conn.close()
    
    #placeholders = ?
    #insert into users: values stored in users.db with sql statement
    
    
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
    
    
    
def delete_user(email, password):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    
    if user and user[4] == password:
        # Delete user's projects
        cursor.execute('DELETE FROM projects WHERE user_id = ?', (user[0],))
        
        # Delete user's classes
        cursor.execute('DELETE FROM classes WHERE user_id = ?', (user[0],))
        
        # Delete user's todos
        cursor.execute('DELETE FROM todos WHERE user_id = ?', (user[0],))
        
        # Delete user
        cursor.execute('DELETE FROM users WHERE email = ?', (email,))
        
        conn.commit()
        conn.close()
        return True
    
    conn.close()
    return False


#projects/classes/to-dos functionality, add and delete

def insert_project(user_id, name):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO projects (user_id, name) VALUES (?, ?)', (user_id, name))
    conn.commit()
    conn.close()

def delete_project(project_id):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM projects WHERE id = ?', (project_id,))
    conn.commit()
    conn.close()

def insert_class(user_id, name):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO classes (user_id, name) VALUES (?, ?)', (user_id, name))
    conn.commit()
    conn.close()

def delete_class(class_id):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM classes WHERE id = ?', (class_id,))
    conn.commit()
    conn.close()

def insert_todo(user_id, name):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO todos (user_id, name) VALUES (?, ?)', (user_id, name))
    conn.commit()
    conn.close()

def delete_todo(todo_id):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()

