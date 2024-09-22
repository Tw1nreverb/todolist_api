from datetime import datetime, timezone

from src.domain.model import Task
from src.uow.task.uow import FakeUOW


async def test_login():
    task = Task(name='Do something',
                date_start=datetime(2024, 5, 1, 12, 0, 0,
                                    tzinfo=timezone.utc),
                date_end=datetime(2024, 10, 10))
    uow = FakeUOW()
    async with uow:
        uow.tasks.add(task)
        await uow.commit()
    expected = await uow.tasks.get(name='Do something')
    assert expected == task
