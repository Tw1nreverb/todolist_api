from datetime import datetime
from jose import jwt
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
from passlib.context import CryptContext
from src.config import get_auth_data
from src.model import Status, Task, User
from src.uow.task.uow import SqlAlchemyUOW as TaskSqlAlchemyUOW
from src.uow.user.uow import SqlAlchemyUOW as UserSqlAlchemyUOW
from src.session import async_session_maker

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class TaskDTO(BaseModel):
    id: int
    name: str
    status: Status
    date_start: datetime
    date_end: datetime


class UserDTO(BaseModel):
    id: int
    email: str
    password: str


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def get_task(id: int) -> TaskDTO:
    uow = TaskSqlAlchemyUOW(async_session_maker)
    task: Task
    async with uow:
        task = await uow.tasks.get(id)
        await uow.commit()
    return task_to_DTO(task)


async def get_user_by_email(email: str):
    uow = UserSqlAlchemyUOW(async_session_maker)
    user: User
    async with uow:
        user = await uow.users.get(email)
        await uow.commit()
    return user


async def add_user(user_dict):
    uow = UserSqlAlchemyUOW(async_session_maker)
    async with uow:
        user = User(email=user_dict["email"], password=user_dict["password"])
        uow.users.add(user)
        await uow.commit()


def task_to_DTO(task: Task) -> TaskDTO:
    return TaskDTO(
        id=task.id,  # pyright: ignore
        name=task.name,
        status=task.status,
        date_start=task.date_start,
        date_end=task.date_end,  # pyright: ignore
    )


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})
    auth_data = get_auth_data()
    encode_jwt = jwt.encode(
        to_encode, auth_data["secret_key"], algorithm=auth_data["algorithm"]
    )
    return encode_jwt
