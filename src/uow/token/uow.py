import abc

from src.db.orm import start_mappers
from src.db.session import async_session_maker
from src.repositories.token import repository
from sqlalchemy.orm import clear_mappers


class AbstractUOW:
    tokens: repository.AbstractRepository

    async def __aexit__(self, *args):
        await self.rollback()

    @abc.abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    async def rollback(self):
        raise NotImplementedError


class SqlAlchemyUOW(AbstractUOW):
    def __init__(self, session_maker=async_session_maker) -> None:
        self._async_session_maker = session_maker

    async def __aenter__(self):
        start_mappers()
        self._session = self._async_session_maker()
        self.users = repository.SqlAlchemyRepository(self._session)
        return self

    async def __aexit__(self, *args):
        await super().__aexit__(*args)
        await self._session.close()
        clear_mappers()

    async def commit(self):
        await self._session.commit()

    async def rollback(self):
        await self._session.rollback()


class FakeUOW(AbstractUOW):
    def __init__(self) -> None:
        self.users = repository.FakeRepository([])
        self.committed = False

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass

    async def commit(self):
        self.committed = True

    async def rollback(self):
        pass
