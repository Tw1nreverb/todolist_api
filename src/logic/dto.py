from datetime import datetime

from pydantic import BaseModel

from src.domain.model import Status, Task


class TaskDTO(BaseModel):
    id: int
    name: str
    status: Status
    date_start: datetime
    date_end: datetime


class AddUserDTO(BaseModel):
    email: str
    password: str


def task_to_DTO(task: Task) -> TaskDTO:
    return TaskDTO(
        id=task.id,  # pyright: ignore
        name=task.name,
        status=task.status,
        date_start=task.date_start,
        date_end=task.date_end,  # pyright: ignore
    )
