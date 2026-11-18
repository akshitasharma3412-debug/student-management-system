import sqlite3
connection = sqlite3.connect("student_tasks.db")
print("Database connected successfully!")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed INTEGER DEFAULT 0
)
""")
print("Tasks table created successfully!")

cursor.execute(
    "SELECT * FROM tasks WHERE title = ?",
    ("Learn Python",)
)

existing_task = cursor.fetchone()
if existing_task is None:
    cursor.execute(
        "INSERT INTO tasks (title, completed) VALUES (?, ?)",
        ("Learn Python", 0)
    )
    connection.commit()
    print("Task inserted successfully!")
else:
    print("Task already exists!")


cursor.execute("SELECT * FROM tasks")
all_tasks = cursor.fetchall()
print("\nAll Tasks:")
for task in all_tasks:
    print(task)


cursor.execute(
    "UPDATE tasks SET title = ? WHERE id = ?",
    ("Advanced Python", 1)
)
connection.commit()
print("Task updated successfully!")
cursor.execute("SELECT * FROM tasks WHERE id = ?", (1,))
updated_task = cursor.fetchone()
print("Updated Task:", updated_task)


cursor.execute(
    "DELETE FROM tasks WHERE id = ?",
    (2,)
)
connection.commit()
print("Task deleted successfully!")
cursor.execute("SELECT * FROM tasks")
remaining_tasks = cursor.fetchall()
print("Remaining Tasks:")
for task in remaining_tasks:
    print(task)


connection.close()
print("Database connection closed!")
