# store in separate class file for organizational purposes and clean code

import sqlite3

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
    
def delete_account(email, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    
    if user and user[4] == password:
        cursor.execute('DELETE FROM users WHERE email = ?', (email,))
        conn.commit()
        conn.close()
        return True
    
    conn.close()
    return False
