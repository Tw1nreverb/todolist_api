from src.logic.dto import TaskDTO, task_to_DTO
from src.domain.model import Task, User
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
