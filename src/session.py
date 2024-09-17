from sqlalchemy.ext.asyncio import create_async_engine 
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import  sessionmaker
from src.config import settings

engine = create_async_engine(
    settings.DB_URL,
    echo=True,
)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False) # pyright: ignore

