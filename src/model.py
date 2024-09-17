from datetime import datetime, timezone
from enum import Enum

class Status(str, Enum):
    in_progress = 'in_progress'
    to_do = 'to-do'
    complete = 'complete'
    canceled = 'canceled'


class Task:

    def __init__(self,
                 name: str,
                 date_start: datetime | None = None,
                 date_end: datetime | None = None) -> None:
        self.__name = name
        self.__date_start = date_start if date_start else datetime.now(
            timezone.utc)
        self.__date_end = date_end
        self.__status = Status.in_progress if datetime.now(
            timezone.utc) >= date_start else Status.to_do

    def to_do(self):
        self.__status = Status.to_do

    def complete(self):
        self.__status = Status.complete

    def cancel(self):
        self.__status = Status.canceled

    def in_progress(self):
        self.__status = Status.in_progress

    def get_status(self) -> Status:
        return self.__status

    def get_name(self) -> str:
        return self.__name


class User:

    def __init__(self, name: str, password: str, email: str) -> None:
        self.__name = name
        self.__password = password
        self.__email = email
    def get_password(self) -> str:
        return self.__password
