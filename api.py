from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
class TaskCreate(BaseModel):
    title:str

class TaskUpdate(BaseModel):
    title: str

@app.get("/")
def home():
    return{"message":"Welcome to Student Task Manager API"}

tasks = []

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: TaskCreate):

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": False
    }

    tasks.append(new_task)

    return new_task

@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    return {"message": "Task not found"}


@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):

    for existing_task in tasks:
        if existing_task["id"] == task_id:
            existing_task["title"] = task.title
            return existing_task

    return {"message": "Task not found"}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}

    return {"message": "Task not found"}



