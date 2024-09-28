from src.domain.model import User
from src.logic.service import login, add_user, register
from src.uow import uow

async def test_login():
    unit_of_work = uow.FakeUOW()
    request_dict = {'email': '<EMAIL>', 'password': '<PASSWORD>'}
    await register(email=request_dict['email'], password=request_dict['password'], uow=unit_of_work)
    assert await login(request_dict['email'], request_dict['password'], unit_of_work) is True
    assert await login(email=request_dict['email'], password='aboba', uow=unit_of_work) is False

async def test_create_refresh_token():
    unit_of_work = uow.FakeUOW()
    request_dict = {'email': '<EMAIL>', 'password': '<PASSWORD>'}
    await register(email=request_dict['email'], password=request_dict['password'], uow=unit_of_work)
    if_login = await login(request_dict['email'], request_dict['password'], unit_of_work)
    assert if_login is True
