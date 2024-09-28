from abc import ABC, abstractmethod

from sqlalchemy import select

from src.domain.model import RefreshToken


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, token: RefreshToken) -> None:
        raise NotImplementedError

    async def get(self, id: str) -> RefreshToken:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session) -> None:
        self.session = session

    def add(self, token: RefreshToken) -> None:
        self.session.add(token)

    async def get(self, id: str) -> RefreshToken:
        statement = select(RefreshToken).filter_by(id=id)
        execute = await self.session.execute(statement)
        result = execute.scalars().one()
        return result


class FakeRepository(AbstractRepository):
    def __init__(self, token) -> None:
        self._tokens = set(token)

    def add(self, task) -> None:
        self._tokens.add(task)

    async def get(self, refresh_token) -> RefreshToken:
        return next(token for token in self._tokens if token.refresh_token == refresh_token)
