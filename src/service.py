import bcrypt
from pydantic import BaseModel

from src.model import Task
from src.uow import SqlAlchemyUOW
from src.session import async_session_maker


def get_hashed_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


async def get_task(id: int):
    uow = SqlAlchemyUOW(async_session_maker)
    task: Task 
    async with uow:
        task = await uow.tasks.get(id)
        await uow.commit()
    return task
        

class TaskDTO(BaseModel):
    id: int
    name: str
    date_start: str
    date_end: str
