tasks=[]
while True:
   print("--------------------------------------------------")
   print("Student Task Manager")
   print("--------------------------------------------------")
   print("1.Add Task")
   print("2.View Task")
   print("3.Mark Task as completed")
   print("4.Update Task")
   print("5.Exit")

   choice=input("Enter your choice:")

   if choice=='1':
    
    task_name=input("Enter your Task:")
    tasks.append({
       "title":task_name,
       "completed":False})
    print("Task added successfully")

   elif choice=='2':
    if not tasks:
      print("No tasks available")
    else:
      print("Your tasks:")
      for index,task in enumerate(tasks,start=1):
        status="Completed" if task["completed"] else "Pending"
        print(index,task["title"],"-",status)
    
   elif choice=='3':
    if not tasks:
      print("No tasks availabale!")
    else:
      for index,task in enumerate(tasks,start=1):
         print(index,task["title"],"-","Completed" if task["completed"] else "Pending")
         
      try:
       task_number=int(input("Enter task number to complete:"))
      except ValueError:
        print("Please enter a valid number!")
        continue
         
      if 1 <= task_number <= len(tasks):
         if tasks[task_number - 1]["completed"]:
          print("Task is already completed!")
         else:
          tasks[task_number - 1]["completed"] = True
          print("Task marked as completed!")
      else:
          print("Invalid task number!")

   elif choice=='4':
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

   elif choice=='5':
    print("Exiting the program")
    break
 
   else:
    print("Invalid choice!")

 



