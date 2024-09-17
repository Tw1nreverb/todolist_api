from src.service import TaskDTO


def test_get_one_task(client):
    response = client.get("/task")
    mock_task = TaskDTO(id=1, name="do", date_start="2024-09-01", date_end="2024-09-02")
    assert response.json() == mock_task.model_dump()
