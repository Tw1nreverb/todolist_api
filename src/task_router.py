from fastapi import APIRouter

router = APIRouter(
    prefix='/task',
    tags=['Task'],
)


@router.get('/')
async def get_hello_world():
    mock_task = {
        "id": 1,
        "name": "do",
        "date_start": "2024-09-01",
        "date_end": "2024-09-02",
    }
    return mock_task
