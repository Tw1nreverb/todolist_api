from datetime import datetime
from jose import jwt
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
from passlib.context import CryptContext
from src.config import get_auth_data
from src.model import Status, Task
from src.uow import SqlAlchemyUOW
from src.session import async_session_maker

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class TaskDTO(BaseModel):
    id: int
    name: str
    status: Status
    date_start: datetime
    date_end: datetime


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password) 

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

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
def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})
    auth_data = get_auth_data()
    encode_jwt = jwt.encode(to_encode, auth_data['secret_key'], algorithm=auth_data['algorithm'])
    return encode_jwt
