from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from src.logic.service import (
    add_user,
    get_authenticated_user,
    create_access_token,
    get_user_by_email,
)
from src.logic.hash import get_password_hash
from src.logic.dto import AddUserDTO

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/register")
async def register_user(user_data: AddUserDTO):
    user = await get_user_by_email(user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь уже существует",
        )
    user_dict = user_data.model_dump()
    user_dict["password"] = get_password_hash(user_data.password)
    await add_user(user_dict)
    return {"message": "Registred"}


@router.post("/login")
async def login_user(user_data: OAuth2PasswordRequestForm = Depends()):
    auth_user = await get_authenticated_user(
        email=user_data.username, password=user_data.password
    )
    if auth_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверная почта или логин",
        )
    access_token = create_access_token(
        data={
            "sub": auth_user.email,
        },
        expires_delta=timedelta(minutes=30),
    )
    return {"access_token": access_token, "refresh_token": None}
