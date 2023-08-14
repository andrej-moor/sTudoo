import sqlite3
# from passlib.hash import bcrypt

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
    conn.commit()
    conn.close()
    
   # Cursor-Objekt kann mit der Datenbank interagieren z.B. zum Erstellen, Einfügen, Abrufen von Daten
   # ID wird automatisch zum Primärschlüssel
   # Email muss UNIQUE also eindeutig sein und darf nicht doppelt vorkommen
   # Commit speichert Änderungen
   # Close schließt die Verbindung
    
def create_classes_table():
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS classes (
            class_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT NOT NULL,
            completed BOOLEAN DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()

    # Foreign Key = USER ID, damit bekannt ist, welchem User das Fach angehört
    # Completed boolean auf default 0, dh auf default "not checked"

def create_projects_table():
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            project_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            class_id INTEGER,
            name TEXT NOT NULL,
            completed BOOLEAN DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (class_id) REFERENCES classes (class_id)
        )
    ''')
    conn.commit()
    conn.close()
    
    # Foreign key = USER ID, damit Projects einem USER zugeordnet sind 
    # Foreign key = Class ID, damit Projects einem Fach zugeordnet sind
    # Completed boolean auf default 0, dh auf default "not checked"

    
    
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
            completed BOOLEAN DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (class_id) REFERENCES classes (class_id),
            FOREIGN KEY (project_id) REFERENCES projects (project_id)
        )
    ''')
    conn.commit()
    conn.close()
    
    # Foreign key = USER ID, damit Todos einem USER zugeordnet sind 
    # Foreign key = Project ID, damit Todos einem Project zugeordnet sind
    # Foreign key = Class ID, damit Todos einem Fach zugeordnet sind
    # Completed boolean auf default 0, dh auf default "not checked"




# ==== USER ACCOUNT RELATED ====

def insert_user(first_name, last_name, email, password):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    
    # hashed_password = bcrypt.hash(password)
    # bcrypt import nicht erkannt, daher nicht funktional
    
    cursor.execute('INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)',
                   (first_name, last_name, email, password)) # hashed_password
    conn.commit()
    conn.close()
    
    # Platzhalter = ?, damit die entsprechenden Werte an der richtigen Stelle in der DB eingefügt werden   

   
   
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

def get_last_name(user_id):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('SELECT last_name FROM users WHERE id = ?', (user_id,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        return None

def get_email(user_id):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('SELECT email FROM users WHERE id = ?', (user_id,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        return None
 
    # get_first_name, get_last_name, get_email zum Anzeigen der Daten auf der User-Startseite
    # oder Useraccount-Seite
    
    
    
 
def delete_user(email, password):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    
    if user and user[4] == password:
    # user [4] vergleicht, ob USER und PW (5. Spalte) miteinander übereinstimmen    
        
        cursor.execute('DELETE FROM projects WHERE user_id = ?', (user[0],))
        cursor.execute('DELETE FROM classes WHERE user_id = ?', (user[0],))
        cursor.execute('DELETE FROM todos WHERE user_id = ?', (user[0],))
        cursor.execute('DELETE FROM users WHERE email = ?', (email,))
        # nach Eingabe von Email und PW den USER
        # mit abhängigen Classes, Projects und Todos löschen
        
        conn.commit()
        conn.close()
        return True
    
    conn.close()
    return False


# ==== CLASSES, PROJECTS & TODOS INSERT AND DELETE ====



def insert_class(user_id, name):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO classes (user_id, name, completed) VALUES (?, ?, 0)', (user_id, name))
    # Classes mit foreign key (USER ID), Class-Name und Completed Status einfügen
    
    conn.commit()
    conn.close()
    return False

def insert_project(user_id, class_id, name):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()

    cursor.execute('SELECT class_id FROM classes WHERE class_id = ? AND user_id = ?', (class_id, user_id))
    class_exists = cursor.fetchone()
    # cursor fetchone ruft ab, ob bereits eine class in der datenbank angelegt ist
    # Project mit foreign key (USER ID & CLASS ID), Project-Name und Completed Status einfügen


    if class_exists:
        cursor.execute('INSERT INTO projects (user_id, class_id, name) VALUES (?, ?, ?)', (user_id, class_id, name))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False
        # Class nicht vorhanden? Error
        
        

def insert_todo(user_id, class_id, project_id, name):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()

    
    cursor.execute('SELECT class_id FROM classes WHERE class_id = ? AND user_id = ?', (class_id, user_id))
    class_exists = cursor.fetchone()
    # Dropdown-List mit für den USER verfügbaren Classes füllen
    # fetchone überprüft, ob bereits eine Class angelegt ist, sonst leere Dropdown-Liste


    cursor.execute('SELECT project_id FROM projects WHERE project_id = ? AND class_id = ?', (project_id, class_id))
    project_exists = cursor.fetchone()
    # Dropdown-List mit für die Classes verfügbaren Projects füllen
    # fetchone überprüft, ob bereits ein project angelegt ist, sonst leere Dropdown-Liste

    if class_exists and project_exists:
        cursor.execute('INSERT INTO todos (user_id, class_id, project_id, name) VALUES (?, ?, ?, ?)',
                       (user_id, class_id, project_id, name))
        # Todo mit foreign key (USER ID, CLASS ID, PROJECT ID) und Todos-Name einfügen
        
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False


def delete_class(class_id):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM classes WHERE class_id = ?', (class_id,))
    cursor.execute('DELETE FROM projects WHERE class_id = ?', (class_id,))
    cursor.execute('DELETE FROM todos WHERE class_id = ?', (class_id,))
    # Class mit abhängigen Projects und Todos löschen
    
    conn.commit()
    conn.close()

def delete_project(project_id):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM projects WHERE project_id = ?', (project_id,))
    cursor.execute('DELETE FROM todos WHERE project_id = ?' , (project_id,))
    # Project mit abhängigen Todos löschen
    
    conn.commit()
    conn.close()


def delete_todo(todo_id):
    conn = sqlite3.connect(CLASSES_DB)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM todos WHERE todo_id = ?', (todo_id,))
    conn.commit()
    conn.close()


