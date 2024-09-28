import uuid
from datetime import datetime, timezone
from enum import Enum


class Status(str, Enum):
    in_progress = "in_progress"
    to_do = "to-do"
    complete = "complete"
    canceled = "canceled"


class Task:
    def __init__(self, name: str, user_id: str, date_start: datetime | None = None,
                 date_end: datetime | None = None) -> None:
        self.id = str(uuid.uuid4())
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


class User:
    def __init__(self, email: str, password: str) -> None:
        self.id = str(uuid.uuid4())
        self.email = email
        self.password = password


class RefreshToken:
    def __init__(self, user_id: str, refresh_token: str) -> None:
        self.user_id = user_id
        self.refresh_token = refresh_token
