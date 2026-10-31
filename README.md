# student-management-system
A python based student based python management system project
# Student Task Manager

## Introduction

Student Task Manager is a beginner-friendly Python project developed to manage student tasks using Object-Oriented Programming (OOP).

The application allows users to add tasks, view their tasks, mark tasks as completed, and update task titles through a simple menu-driven interface.

## Objective

The objective of this project is to practice Python programming, classes and objects, methods, lists, and basic error handling.
## Features

- **Add Task:** Add a new task to the task list.
- **View Tasks:** Display all tasks with their current status.
- **Mark Task as Completed:** Mark a pending task as completed.
- **Update Task:** Change the title of an existing task.
- **Input Validation:** Prevent empty task titles.
- **Error Handling:** Handle invalid task numbers and non-numeric input.
- **Menu-Driven Interface:** Navigate through the application using menu options.

## Technologies Used

- **Language:** Python
- **Concepts:** Object-Oriented Programming (OOP), Classes, Objects, Methods, Lists, Conditional Statements, and Loops.
- **Error Handling:** `try-except` blocks
- **Version Control:** Git
- **Code Hosting:** GitHub

## How to Run

1. Install Python on your computer.
2. Clone or download this repository.
3. Open the project folder in VS Code or a terminal.
4. Run the Python file containing the `TaskManager` class and the `manager.run()` call.

Example:

```bash
python task_manager2.py
```

*Note: Replace `task_manager2.py` with the actual filename containing your OOP version, if different.*
## Testing

The following test cases were used to check the basic functionality of the Student Task Manager.

| Test Case | Expected Result |
|---|---|
| Add a new task | Task should be added successfully. |
| View tasks | All available tasks should be displayed. |
| Mark a task as completed | Task status should change to Completed. |
| Update a task title | The task title should be updated successfully. |
| Enter an invalid task number | An error message should be displayed. |
| Enter a non-numeric task number | The application should handle the invalid input. |
| Add an empty task title | The application should display a validation message. |
| Exit the application | The application should terminate successfully. |

*Note: Run each test case and update this section according to the actual results.*
## Project Structure

```text
student_management_system/
│
├── main.py
├── task_manager.py
├── task_manager2.py
└── README.md
```

### File Description

- **main.py:** Entry point of the application, if used to start the program.
- **task_manager.py:** Contains the basic function-based version of the Student Task Manager.
- **task_manager2.py:** Contains the Object-Oriented Programming (OOP) version of the project.
- **README.md:** Provides project information, features, technologies, and testing details.
- ## Learning Outcomes

Through this project, I practiced the following concepts:

- Understanding Python classes and objects.
- Creating and using methods.
- Managing tasks using lists and objects.
- Implementing conditional statements and loops.
- Validating user input.
- Handling errors using `try-except`.
- Implementing task creation, viewing, completion, and updating features.
- Using Git for version control.
- Uploading and maintaining project files on GitHub.
- Writing project documentation using Markdown.

## Future Improvements

- Store tasks permanently using a database.
- Add task deletion functionality.
- Develop a graphical user interface.
- Build a web-based version of the application.
