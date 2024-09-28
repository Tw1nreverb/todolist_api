from src.logic.service import login, register
from src.uow import uow


async def test_login():
    unit_of_work = uow.FakeUOW()
    request_dict = {'email': '<EMAIL>', 'password': '<PASSWORD>'}
    await register(email=request_dict['email'], password=request_dict['password'], uow=unit_of_work)
    login_data = await login(request_dict['email'], request_dict['password'],uow=unit_of_work)
    refresh_token = await unit_of_work.tokens.get(str(login_data['refresh_token'].refresh_token))
    assert login_data['refresh_token'].refresh_token == refresh_token.refresh_token
    assert await login(email=request_dict['email'], password='aboba', uow=unit_of_work) is False


