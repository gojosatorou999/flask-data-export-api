import sqlite3

def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    # Create a dummy users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        role TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Insert some dummy data if the table is empty
    cursor.execute('SELECT COUNT(*) FROM users')
    if cursor.fetchone()[0] == 0:
        users = [
            ('Alice Smith', 'alice@example.com', 'Admin'),
            ('Bob Jones', 'bob@example.com', 'User'),
            ('Charlie Brown', 'charlie@example.com', 'Editor'),
            ('Diana Prince', 'diana@example.com', 'User'),
            ('Ethan Hunt', 'ethan@example.com', 'Security')
        ]
        cursor.executemany('INSERT INTO users (name, email, role) VALUES (?, ?, ?)', users)
        print("Inserted dummy data.")
    
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == '__main__':
    init_db()
