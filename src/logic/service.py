from src.domain.model import Task, User
from src.logic.dto import TaskDTO, task_to_DTO
from src.logic.hash import get_password_hash, verify_password
from src.uow.task.uow import AbstractUOW as TaskAbstractUOW
from src.uow.user.uow import AbstractUOW as UserAbstractUOW


async def get_task(id: int,uow:TaskAbstractUOW) -> TaskDTO:
    task: Task
    async with uow:
        task = await uow.tasks.get(id)
        await uow.commit()
    return task_to_DTO(task)


async def get_user_by_email(email: str,uow: UserAbstractUOW) -> User:
    user: User
    async with uow:
        user = await uow.users.get(email)
        await uow.commit()
    return user


async def add_user(uow: UserAbstractUOW, **user_dict):
    async with uow:
        user = User(email=user_dict["email"], password=user_dict["password"])
        uow.users.add(user)
        await uow.commit()


async def register(email: str, password: str, uow: UserAbstractUOW) -> bool:
    try:
        user = await get_user_by_email(email=email,uow=uow)
        if user:
            return False
    except:
        pass
    password = get_password_hash(password)
    await add_user(uow=uow,email=email,password=password)
    return True

async def login(email: str, password: str, uow: UserAbstractUOW) -> bool:
    user = await get_user_by_email(email=email,uow=uow)
    if verify_password(plain_password=password, hashed_password=user.password):
        return True
    else:
        return False
