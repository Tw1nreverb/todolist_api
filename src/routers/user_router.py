from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from src.logic.service import (
    add_user,
    get_user_by_email,
)
from src.logic.hash import get_password_hash
from src.logic.dto import AddUserDTO

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/register")
async def register_user():
    return {"Hello1":1234}


@router.post("/login")
async def login_user():
    return {"Hello":123}
