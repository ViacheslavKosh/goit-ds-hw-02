import sqlite3

def create_db():
    try:
    # читаємо файл зі скриптом для створення БД
        with open('users.sql', 'r') as f:
            sql = f.read()
        
    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
        with sqlite3.connect('task_management.db') as con:
            cur = con.cursor()
    # виконуємо скрипт із файлу, який створить таблиці в БД        
            cur.executescript(sql)

    except sqlite3.Error as e:
        print("Error:", e)

if __name__ == "__main__":
    create_db()
