from abc import ABC, abstractmethod
from . import model


class AbstractRepository(ABC):

    @abstractmethod
    def add(self, task: model.Task):
        raise NotImplementedError

    def get(self, id: int) -> model.Task:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session) -> None:
        self.session = session

    def add(self, task):
        self.session.add(task)

    def get(self, id):
        return self.session.query(model.Task).filter_by(id=id).one()
