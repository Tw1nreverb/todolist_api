from abc import ABC, abstractmethod
from src.model import User 
from sqlalchemy import select


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> None:
        raise NotImplementedError

    async def get(self, email: str) -> User:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session) -> None:
        self.session = session

    def add(self, user) -> None:
        self.session.add(user)

    async def get(self, email: str) -> User:
        statement = select(User).filter_by(email=email)
        execute = await self.session.execute(statement)
        result = execute.scalars().one()
        return result
