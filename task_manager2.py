from task import Task
class TaskManager:
    def __init__(self):
     self.tasks=[] 

    def add_task(self,title):
        if not title.strip():
           print("Tasks title cannot be empty!")
           return
        task=Task(title)
        self.tasks.append(task)
        print("Task added successfully")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available")
            return
        for index, task in enumerate(self.tasks,start=1):
            status="Completed" if task.completed else "Pending"
            print(index,task.title,"-",status)

    def mark_completed(self):
     if not self.tasks:
        print("No tasks available!")
        return

     self.view_tasks()

     try:
        task_number = int(input("Enter task number to complete: "))
     except ValueError:
        print("Please enter a valid number!")
        return

     if 1 <= task_number <= len(self.tasks):
        task = self.tasks[task_number - 1]
        task.mark_completed()
        print("Task marked as completed!")
     else:
        print("Invalid task number!")

    def update_task(self):
     if not self.tasks:
        print("No tasks available!")
        return

     self.view_tasks()

     try:
        task_number = int(input("Enter task number to update: "))
     except ValueError:
        print("Please enter a valid number!")
        return

     if 1 <= task_number <= len(self.tasks):
        new_title = input("Enter new task title: ")
        if not new_title.strip():
           print("Task title cannot be empty!")
           return

        task = self.tasks[task_number - 1]
        task.update_title(new_title)

        print("Task updated successfully!")
     else:
        print("Invalid task number!")

    def run(self):
     while True:
        print("\n===== STUDENT TASK MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Update Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            self.add_task(title)

        elif choice == "2":
            self.view_tasks()

        elif choice == "3":
            self.mark_completed()

        elif choice == "4":
            self.update_task()

        elif choice == "5":
            print("Thank you for using Student Task Manager!")
            break

        else:
            print("Invalid choice! Please select 1-5.")

manager=TaskManager()
manager.run()





