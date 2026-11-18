from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to Student Task Manager API"
    }

def test_create_task():
    response = client.post(
        "/tasks",
        json={"title": "Pytest Practice"}
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Pytest Practice"
    assert response.json()["completed"] == 0

def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_task_by_id():
    create_response = client.post(
        "/tasks",
        json={"title": "Test Task"}
    )

    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id
    assert response.json()["title"] == "Test Task"

def test_update_task():
    create_response = client.post(
        "/tasks",
        json={"title": "Old Task"}
    )

    task_id = create_response.json()["id"]

    response = client.patch(
        f"/tasks/{task_id}",
        json={
            "title": "Updated Task",
            "completed": True
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task"
    assert response.json()["completed"] == 1

def test_delete_task():
    create_response = client.post(
        "/tasks",
        json={"title": "Task to Delete"}
    )

    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404

def test_create_task_with_empty_title():
    response = client.post(
        "/tasks",
        json={"title": ""}
    )

    assert response.status_code == 422

def test_create_task_with_spaces_only():
    response = client.post(
        "/tasks",
        json={"title": "     "}
    )

    assert response.status_code == 422

def test_get_nonexistent_task():
    response = client.get("/tasks/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

def test_update_nonexistent_task():
    response = client.patch(
        "/tasks/99999",
        json={
            "title": "Updated Task",
            "completed": True
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

def test_delete_nonexistent_task():
    response = client.delete("/tasks/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"