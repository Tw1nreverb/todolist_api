from fastapi import APIRouter

from src.service import get_task


router = APIRouter(
    prefix="/task",
    tags=["Task"],
)


@router.get("/{id}")
async def show_task(id:int):
    task = await get_task(id)
    return task
