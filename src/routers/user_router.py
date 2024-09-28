from fastapi import APIRouter

from src.logic.service import (
    register,
)
from src.uow import uow as unit_of_work
router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/register")
async def register_user(email: str, password: str):
    result = await register(email=email, password=password, uow=unit_of_work.SqlAlchemyUOW())
    return result


@router.post("/login")
async def login_user():
    return {"Hello": 123}

# async def test_register_user(email: str, password: str):
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
