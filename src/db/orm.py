from sqlalchemy import Table, Column, Integer, String, DateTime, Enum as SQLAlchemyEnum
from sqlalchemy.orm import registry
from src.domain.model import Status, Task, User

mapper_registry = registry()
metadata = mapper_registry.metadata
task_table = Table(
    "task",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100)),
    Column("status", SQLAlchemyEnum(Status)),
    Column("date_start", DateTime),
    Column("date_end", DateTime),
)
user_table = Table(
    "user",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(100)),
    Column("password", String(100)),
    Column('refresh_toker', String(200)),
)


def start_mappers():
    mapper_registry.map_imperatively(Task, task_table)
    mapper_registry.map_imperatively(User, user_table)
