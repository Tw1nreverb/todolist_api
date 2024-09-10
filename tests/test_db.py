from datetime import datetime, timezone
from src.repository import SqlAlchemyRepository 
from src.model import Task
from src.config import settings 
def test_setup_db(session):
    repo = SqlAlchemyRepository(session)
    task = Task(name='Do something',
                date_start=datetime(2024, 5, 1, 12, 0, 0,
                                    tzinfo=timezone.utc),
                date_end=datetime(2024, 10, 10))
    repo.add(task)
    print(repo.get('Do something'))
    
