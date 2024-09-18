from fastapi import APIRouter, HTTPException, status

from src.service import UserDTO, add_user, get_password_hash, get_user_by_email

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/register")
async def register_user(user_data: UserDTO):
    user = await get_user_by_email(user_data.email) 
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует',
        )
    user_dict = user_data.model_dump()
    user_dict['password'] = get_password_hash(user_data.password)
    await add_user(user_dict)  
    return {'message':'Registred'}
