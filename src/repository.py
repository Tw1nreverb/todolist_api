from abc import ABC, abstractmethod
from src.model import Task 
from sqlalchemy import select

class AbstractRepository(ABC):

    @abstractmethod
    def add(self, task: Task):
        raise NotImplementedError

    async def get(self, id: int) -> Task:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session) -> None:
        self.session = session

    def add(self, task):
        self.session.add(task)

    async def get(self, id):
        statement = select(Task).filter_by(id=id)
        execute = await self.session.execute(statement)
        result = execute.scalars().one()
        return result
