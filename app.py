from flask import Flask
import sqlite3

app = Flask(__name__)

# Database Connection Function
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row   # Allows accessing columns by name
    return conn

# Create Users Table

def create_users_table():
    conn = get_db_connection()

    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


create_users_table()



@app.route('/')
def home():
    return "Hello, World! Flask App is Running "



if __name__ == '__main__':
    app.run(debug=True)