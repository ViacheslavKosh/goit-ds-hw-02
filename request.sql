-- Отримати всі завдання певного користувача за його user_id.
SELECT * FROM tasks WHERE user_id = ?;

-- Вибрати завдання за певним статусом (наприклад, 'new').
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');

-- Оновити статус конкретного завдання на 'in progress' або інший статус.
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = ?;

-- Отримати список користувачів, які не мають жодного завдання.
SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

-- Додати нове завдання для конкретного користувача.
INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?);

-- Отримати всі завдання, які ще не завершено.
SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

-- Видалити конкретне завдання за його id.
DELETE FROM tasks WHERE id = ?;

-- Знайти користувачів з певною електронною поштою.
SELECT * FROM users WHERE email LIKE '%@example.com';

-- Оновити ім'я користувача.
UPDATE users SET fullname = ? WHERE id = ?;

-- Отримати кількість завдань для кожного статусу.
SELECT status.name, COUNT(tasks.id) AS task_count
FROM status LEFT JOIN tasks ON status.id = tasks.status_id
GROUP BY status.id;

-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
SELECT tasks.*
FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%@example.com';

-- Отримати список завдань, що не мають опису.
SELECT * FROM tasks WHERE description IS NULL;

-- Вибрати користувачів та їхні завдання, які є у статусі 'in progress'.
SELECT users.fullname, tasks.title
FROM users
JOIN tasks ON users.id = tasks.user_id
JOIN status ON tasks.status_id = status.id
WHERE status.name = 'in progress';

-- Отримати користувачів та кількість їхніх завдань.
SELECT users.fullname, COUNT(tasks.id) AS task_count
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.id;
