from fastapi import APIRouter

router = APIRouter(
    prefix='/task',
    tags=['Task'],
)


@router.get('/')
async def get_hello_world():
    return ({"Hello its me": 123})
