import abc

from sqlalchemy.orm import clear_mappers
from src.repositories.user import repository
from src.orm import start_mappers


class AbstractUOW:
    users: repository.AbstractRepository

    async def __aexit__(self, *args):
        await self.rollback()

    @abc.abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


class SqlAlchemyUOW(AbstractUOW):
    def __init__(self, async_session_maker) -> None:
        self._async_session_maker = async_session_maker

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
