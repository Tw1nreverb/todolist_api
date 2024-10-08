from sqlalchemy import Table, Column, String, DateTime, Enum as SQLAlchemyEnum, ForeignKey, Integer
from sqlalchemy.orm import registry, relationship
from src.domain.model import Status, Task, User, RefreshToken

mapper_registry = registry()
metadata = mapper_registry.metadata
task_table = Table(
    "task",
    mapper_registry.metadata,
    Column("id", String(100), primary_key=True),
    Column("name", String(100)),
    Column("status", SQLAlchemyEnum(Status)),
    Column("date_start", DateTime),
    Column("date_end", DateTime),
    Column('user_id',String(100),ForeignKey('user.id')),
)
user_table = Table(
    "user",
    mapper_registry.metadata,
    Column("id", String(100), primary_key=True),
    Column("email", String(100)),
    Column("password", String(100)),
)
refresh_session_table = Table(
    "refresh_token",
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', String(100), ForeignKey('user.id')),
    Column("refresh_token",String(100)),
)


def start_mappers():
    mapper_registry.map_imperatively(Task, task_table, properties={
        'user': relationship("User", back_populates="tasks"),
    })
    mapper_registry.map_imperatively(User, user_table, properties={
        'tasks': relationship("Task", back_populates="user"),
        'refresh_token': relationship("RefreshToken", back_populates="user")
    })
    mapper_registry.map_imperatively(RefreshToken,refresh_session_table, properties={
        'user': relationship("User", back_populates="refresh_token"),
    })
