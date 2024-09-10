import pytest
from sqlalchemy.orm import clear_mappers, sessionmaker
from src.test_config import test_settings
from sqlalchemy import create_engine
from src.orm import metadata, start_mappers


@pytest.fixture(scope='session',autouse=True)
def engine_db():
    assert test_settings.MODE=="TEST"
    engine = create_engine(test_settings.DB_URL)
    metadata.drop_all(engine)
    metadata.create_all(engine)
    return engine


@pytest.fixture(scope='session',autouse=True)
def session(engine_db):
    start_mappers()
    yield sessionmaker(bind=engine_db)()
    clear_mappers()
