from abc import ABC, abstractmethod

from sqlalchemy.orm import selectinload

from src.domain.model import Task
from sqlalchemy import select


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, task: Task) -> None:
        raise NotImplementedError

    async def get(self, id: str) -> Task:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session) -> None:
        self.session = session

    def add(self, task) -> None:
        self.session.add(task)

    async def get(self, id) -> Task:
        statement = select(Task).filter_by(id=id)
        execute = await self.session.execute(statement)
        result = execute.scalars().one()
        return result

    async def get_users(self, id) -> Task:
        statement = select(Task).filter_by(id=id).options(selectinload(Task.user))
        execute = await self.session.execute(statement)
        result = execute.scalars().one()
        return result


class FakeRepository(AbstractRepository):
    def __init__(self, tasks) -> None:
        self._tasks = set(tasks)

    def add(self, task) -> None:
        self._tasks.add(task)

    async def get(self, name) -> Task:
        return next(task for task in self._tasks if task.name == name)
