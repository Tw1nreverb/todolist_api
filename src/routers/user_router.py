from fastapi import APIRouter
from src.logic.service import (
    add_user, register,
)
from src.uow.user.uow import SqlAlchemyUOW as UserAlchemyUOW

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
    return {"Hello":123}
