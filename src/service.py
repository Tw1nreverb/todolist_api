from datetime import datetime
import bcrypt
from pydantic import BaseModel

from src.model import Status, Task
from src.uow import SqlAlchemyUOW
from src.session import async_session_maker


class TaskDTO(BaseModel):
    id: int
    name: str
    status: Status
    date_start: datetime
    date_end: datetime


def get_hashed_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


async def get_task(id: int) -> TaskDTO:
    uow = SqlAlchemyUOW(async_session_maker)
    task: Task
    async with uow:
        task = await uow.tasks.get(id)
        await uow.commit()
    return task_to_DTO(task)


def task_to_DTO(task: Task) -> TaskDTO:
    return TaskDTO(
        id=task.id, # pyright: ignore
        name=task.name,
        status=task.status,
        date_start=task.date_start,
        date_end=task.date_end, # pyright: ignore
    ) 
