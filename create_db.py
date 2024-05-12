import sqlite3

def create_tables():
    try:
        with sqlite3.connect('task_management.db') as con:
            cur = con.cursor()
            # Таблиця користувачів
            cur.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            fullname VARCHAR(100) NOT NULL,
                            email VARCHAR(100) UNIQUE NOT NULL
                        )''')

            # Таблиця статусів завдань
            cur.execute('''CREATE TABLE IF NOT EXISTS status (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(50) UNIQUE NOT NULL
                        )''')

            # Таблиця завдань
            cur.execute('''CREATE TABLE IF NOT EXISTS tasks (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title VARCHAR(100) NOT NULL,
                            description TEXT,
                            status_id INTEGER,
                            user_id INTEGER,
                            FOREIGN KEY (status_id) REFERENCES status(id) ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE
                        )''')

    except sqlite3.Error as e:
        print("Error:", e)

if __name__ == "__main__":
    create_tables()
