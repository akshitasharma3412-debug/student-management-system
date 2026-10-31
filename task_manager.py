tasks=[]
def add_task():
    task_name=input("Enter your task:")
    tasks.append({
        "title":task_name,
        "completed":False
    })
    print("Task added successfully")

def view_task():
    if not tasks:
     print("No tasks available")
    else:
     print("Your tasks:")
     for index,task in enumerate(tasks,start=1):
            status="Completed" if task["completed"] else "Pending"
            print(index,task["title"],"-",status)

def mark_completed():
   if not tasks:
    print("No tasks availabale!")
   else:
    for index,task in enumerate(tasks,start=1):
     print(index,task["title"],"-","Completed" if task["completed"] else "Pending")
            
    try:
     task_number=int(input("Enter task number to complete:"))
    except ValueError:
      print("Please enter a valid number!")
      return
            
    if 1 <= task_number <= len(tasks):
        if tasks[task_number - 1]["completed"]:
         print("Task is already completed!")
        else:
         tasks[task_number - 1]["completed"] = True
         print("Task marked as completed!")
    else:
         print("Invalid task number!")

def update_task():
    if not tasks:
     print("No tasks available")
    else:
     for index,task in enumerate(tasks,start=1):
      print(index,task["title"])
     task_number=int(input("Enter task number to update:"))
     if 1<=task_number<=len(tasks):
      print("Valid task number")
      new_title=input("Enter new task name:")
      tasks[task_number - 1]["title"]=new_title
      tasks[task_number - 1]["completed"]=False
      print("Task updated successfully!")
     else:
      print("Invalid task number")  

def exit_function():
  print("Exiting Student Task Manager!Goodbye!")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Update Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_task()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        update_task()
    elif choice == '5':
        exit_function()
        break
    else:
        print("Invalid choice!")


   
