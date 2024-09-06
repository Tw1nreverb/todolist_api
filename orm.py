from sqlalchemy import Table, Column, Integer, String, DateTime, Enum as SQLAlchemyEnum
from sqlalchemy.orm import registry
from model import Status, Task

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
mapper_registry.map_imperatively(Task, task_table)
