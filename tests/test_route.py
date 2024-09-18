from datetime import datetime
from src.service import TaskDTO
from src.model import Status

#def test_get_one_task(client):
#    response = client.get("/task")
#    mock_task = TaskDTO(id=1, name="do", status=Status.complete,date_start=datetime(2024,9,1), date_end=datetime(2024,9,2))
#    assert response.json() == mock_task.model_dump()
