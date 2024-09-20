from datetime import datetime, timezone
from domain.model import Status, Task


def test_create_task_and_check_status():
    task = Task(name='Do something',
                date_start=datetime(2024, 5, 1, 12, 0, 0,
                                    tzinfo=timezone.utc),
                date_end=datetime(2024, 10, 10))

    assert task.status == Status.in_progress 
    task.to_do()
    assert task.status == Status.to_do 
    task.complete()
    assert task.status == Status.complete 
    task.cancel()
    assert task.status == Status.canceled 
