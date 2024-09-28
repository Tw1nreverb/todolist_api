from fastapi import APIRouter

from src.logic.service import get_task
from src.uow.task.uow import SqlAlchemyUOW as TaskAlchemyUOW

router = APIRouter(
    prefix="/task",
    tags=["Task"],
)


@router.get("/{id}")
async def show_task(id: int):
    task = await get_task(id, uow=TaskAlchemyUOW())
    return task
