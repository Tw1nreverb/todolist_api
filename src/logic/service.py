from typing import Optional
from jose import jwt
from datetime import datetime, timedelta, timezone
from src.settings.config import get_auth_data
from src.logic.dto import TaskDTO, task_to_DTO
from src.logic.hash import verify_password
from domain.model import Task, User
from src.uow.task.uow import SqlAlchemyUOW as TaskSqlAlchemyUOW
from src.uow.user.uow import SqlAlchemyUOW as UserSqlAlchemyUOW
from src.db.session import async_session_maker


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


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    auth_data = get_auth_data()
    encode_jwt = jwt.encode(
        to_encode, auth_data["secret_key"], algorithm=auth_data["algorithm"]
    )
    return encode_jwt


async def get_authenticated_user(email: str, password: str) -> User | None:
    uow = UserSqlAlchemyUOW(async_session_maker)
    user: User
    async with uow:
        user = await uow.users.get(email)
        await uow.commit()
    if user is None or not verify_password(password, user.password):
        return None
    return user
