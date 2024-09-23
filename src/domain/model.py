import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import Tuple


class Status(str, Enum):
    in_progress = "in_progress"
    to_do = "to-do"
    complete = "complete"
    canceled = "canceled"


class Task:
    def __init__(
            self,
            name: str,
            date_start: datetime | None = None,
            date_end: datetime | None = None,
    ) -> None:
        self.name = name
        self.date_start = date_start if date_start else datetime.now(timezone.utc)
        self.date_end = date_end
        self.status = (
            Status.in_progress
            if datetime.now(timezone.utc) >= date_start
            else Status.to_do
        )

    def to_do(self) -> None:
        self.status = Status.to_do

    def complete(self) -> None:
        self.status = Status.complete

    def cancel(self) -> None:
        self.status = Status.canceled

    def in_progress(self) -> None:
        self.status = Status.in_progress


class User:
    def __init__(self, email: str, password: str) -> None:
        self.password = password
        self.email = email


@dataclass(frozen=True)
class EntityId:
    id: uuid.UUID

    def __composite_values__(self) -> Tuple[str]:
        return (str(self),)

    @classmethod
    def new(cls) -> "EntityId":
        return EntityId(uuid.uuid4())

    @classmethod
    def of(cls, id: str) -> "EntityId":
        return cls(uuid.UUID(hex=id, version=4))
