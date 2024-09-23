from datetime import datetime, timezone

from fastapi import APIRouter

from src.domain.model import Task
from src.logic.service import (
    add_user, register,
)
from src.uow.user.uow import SqlAlchemyUOW as UserAlchemyUOW
from src.uow.task.uow import SqlAlchemyUOW as TaskAlchemyUOW

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/register")
async def register_user(email:str,password:str):
    result = await register(email=email,password=password, uow=UserAlchemyUOW())
    return result


@router.post("/login")
async def login_user():
    return {"Hello": 123}
#async def test_register_user(email: str, password: str):
#    result = await register(email=email, password=password, uow=UserAlchemyUOW())
#    uow = TaskAlchemyUOW()
#    async with uow:
#        uow.tasks.add(Task(name='Do something',
#                           date_start=datetime(2024, 5, 1
#                                               ),
#                           date_end=datetime(2024, 10, 10), user_id=str(17)))
#        task = await uow.tasks.get_users("1a84f3d7-6bc0-4c14-a510-cb85989a3eae")
#        await uow.commit()
#    return task
#    return result
