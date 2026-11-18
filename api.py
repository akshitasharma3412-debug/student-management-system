from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, Field, field_validator

from db_connection import (
    add_task as db_add_task,
    get_tasks as db_get_tasks,
    get_task as db_get_task,
    update_task as db_update_task,
    delete_task as db_delete_task
)

app=FastAPI()
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        if not value.strip():
            raise ValueError("Task title cannot contain only spaces")
        return value.strip()

class TaskUpdate(BaseModel):
    title: str = Field(..., min_length=1)
    completed:bool=False
    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        if not value.strip():
            raise ValueError("Task title cannot contain only spaces")
        return value.strip()

@app.get("/")
def home():
    return{"message":"Welcome to Student Task Manager API"}

@app.get("/tasks")
def read_tasks():
    return db_get_tasks()

@app.post("/tasks")
def create_task(task: TaskCreate):
    task_id = db_add_task(task.title)
    return db_get_task(task_id)

@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    task = db_get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task

@app.patch("/tasks/{task_id}")
def edit_task(task_id: int, task: TaskUpdate):
    updated = db_update_task(
        task_id,
        task.title,
        task.completed
    )
    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return db_get_task(task_id)

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    deleted = db_delete_task(task_id)

    if not deleted:
        raise HTTPException(
        status_code=404,
        detail="Task not found")

    return {"message": "Task deleted successfully"}



