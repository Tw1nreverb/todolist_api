from abc import ABC, abstractmethod

from src.domain.model import User
from sqlalchemy import select


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, user: User):
        raise NotImplementedError

    async def get(self, email: str) -> User:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session) -> None:
        self.session = session

    def add(self, user: User):
        self.session.add(user)

    async def get(self, email: str) -> User:
        statement = select(User).filter_by(email=email)
        execute = await self.session.execute(statement)
        result = execute.scalars().first()
        return result


class FakeRepository(AbstractRepository):
    def __init__(self, users) -> None:
        self._users = set(users)

    def add(self, user) -> None:
        self._users.add(user)

    async def get(self, email) -> User:
        return next(user for user in self._users if user.email == email)
