from datetime import datetime, timezone
from enum import Enum


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
    def __init__(self, name: str, password: str, email: str) -> None:
        self.name = name
        self.password = password
        self.email = email

