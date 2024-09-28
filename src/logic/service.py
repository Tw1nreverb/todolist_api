import uuid
from typing import Union

from src.domain.model import Task, User, RefreshToken, EntityId
from src.logic.dto import TaskDTO, task_to_DTO
from src.logic.hash import get_password_hash, verify_password
from src.uow import uow as unit_of_work


async def get_task(id: int, uow: unit_of_work.AbstractUOW) -> TaskDTO:
    task: Task
    async with uow:
        task = await uow.tasks.get(id)
        await uow.commit()
    return task_to_DTO(task)


async def get_user_by_email(email: str, uow: unit_of_work.AbstractUOW) -> User:
    user: User
    async with uow:
        user = await uow.users.get(email)
        await uow.commit()
    return user


async def add_user(uow: unit_of_work.AbstractUOW, **user_dict):
    async with uow:
        user = User(email=user_dict["email"], password=user_dict["password"])
        uow.users.add(user)
        await uow.commit()


async def register(email: str, password: str, uow: unit_of_work.AbstractUOW) -> bool:
    try:
        user = await get_user_by_email(email=email, uow=uow)
        if user:
            return False
    except:
        pass
    password = get_password_hash(password)
    await add_user(uow=uow, email=email, password=password)
    return True


async def login(email: str, password: str, uow: unit_of_work.AbstractUOW) -> Union[dict[str,RefreshToken], bool]:
    user = await get_user_by_email(email=email, uow=uow)
    if verify_password(plain_password=password, hashed_password=user.password):
        async with uow:
            refresh_token = RefreshToken(user_id=uuid.UUID(user.id),refresh_token=EntityId.new().id)
            uow.tokens.add(refresh_token)
            await uow.commit()
        return {'refresh_token':refresh_token}
    else:
        return False
