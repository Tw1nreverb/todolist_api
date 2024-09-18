from datetime import datetime, timezone
from src.repository import SqlAlchemyRepository 
from sqlalchemy import select
from src.model import Task
from src.orm import task_table
#def test_add_and_get_task(session):
#    repo = SqlAlchemyRepository(session)
#    task = Task(name='Do something',
#                date_start=datetime(2024, 5, 1, 12, 0, 0,
#                                    tzinfo=timezone.utc),
#                date_end=datetime(2024, 10, 10))
#    repo.add(task)
#    session.commit()
#    assert task.name == repo.get(1).get_name()
