from flask import Flask
import sqlite3

app = Flask(__name__)

# Database Connection Function
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row 
    # Allows accessing columns by name
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

#Every time you connect to SQLite,Foreign keys are OFF by default.
# SQLite does NOT enforce foreign key rules unless you enable them.So if you don’t add this:
#ON DELETE CASCADE will NOT work, Tasks may remain even if user is deleted
    

# Create Users Table
def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        );
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            user_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        );
    """)

    conn.commit()
    conn.close()



@app.route('/')
def home():
    return "Hello, World! Flask App is Running "



if __name__ == '__main__':
    app.run(debug=True)