from faker import Faker
import sqlite3

def seed_database():
    fake = Faker()

    # Заповнюємо таблицю користувачів
    users_data = [(fake.name(), fake.email()) for _ in range(10)]

    # Заповнюємо таблицю статусів
    statuses_data = [('new',), ('in progress',), ('completed',)]

    # Заповнюємо таблицю завдань
    tasks_data = [(fake.sentence(), fake.text(), fake.random_int(min=1, max=3), fake.random_int(min=1, max=10)) for _ in range(20)]

    try:
        with sqlite3.connect('task_management.db') as con:
            cur = con.cursor()

            # Заповнюємо таблицю користувачів
            cur.executemany("INSERT INTO users (fullname, email) VALUES (?, ?)", users_data)

            # Заповнюємо таблицю статусів
            cur.executemany("INSERT INTO status (name) VALUES (?)", statuses_data)

            # Заповнюємо таблицю завдань
            cur.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)", tasks_data)

    except sqlite3.Error as e:
        print("Error:", e)

if __name__ == "__main__":
    seed_database()
