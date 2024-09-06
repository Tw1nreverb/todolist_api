from datetime import datetime,timezone 
from ..model import Status, Task
def test_in_progress_to_do_status():
    task = Task(name='Do something',date_start=datetime(2023, 10, 1, 12, 0, 0, tzinfo=timezone.utc),date_end=datetime(2024,10,10))
    assert task.status == Status.in_progress
    task = Task(name='Do something',date_start=datetime(2024, 10, 1, 12, 0, 0, tzinfo=timezone.utc),date_end=datetime(2024,10,10))
    assert task.status == Status.to_do
