from fastapi import APIRouter

from src.service import get_task


router = APIRouter(
    prefix="/task",
    tags=["Task"],
)


@router.get("/")
async def show_task():
    task = await get_task(1)
    return task
