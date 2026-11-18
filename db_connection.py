import sqlite3

def get_connection():
    connection = sqlite3.connect("student_tasks.db")
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
    """)
    connection.commit()
    connection.close()
    print("Tasks table created successfully!")

def add_task(title):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, completed) VALUES (?, ?)",
        (title, 0)
    )
    connection.commit()
    task_id = cursor.lastrowid
    connection.close()
    return task_id

def get_tasks():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    connection.close()
    return [dict(task) for task in tasks]


def get_task(task_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )
    task = cursor.fetchone()
    connection.close()
    return dict(task) if task else None


def update_task(task_id, title,completed):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE tasks SET title = ?, completed=? WHERE id = ?",
        (title,int(completed), task_id)
    )
    connection.commit()
    updated = cursor.rowcount > 0
    connection.close()
    return updated

def delete_task(task_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    deleted = cursor.rowcount > 0
    connection.close()
    return deleted

create_table()
