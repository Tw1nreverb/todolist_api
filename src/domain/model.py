import uuid
from dataclasses import dataclass, field
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
            user_id: str,
            date_start: datetime | None = None,
            date_end: datetime | None = None,
    ) -> None:
        self.id = uuid.uuid4()
        self.user_id = user_id
        self.name = name
        self.date_start = date_start if date_start else datetime.now(timezone.utc)
        self.date_end = date_end
        self.status = (
            Status.in_progress
            if datetime.now() >= date_start
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



@dataclass(frozen=True)
class User:
    email: str
    password: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass(frozen=True)
class RefreshToken:
    user_id: uuid.UUID
    refresh_token: uuid.UUID
