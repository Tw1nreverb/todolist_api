from src.domain.model import User
from src.logic.service import login, add_user, register
from src.uow.user.uow import FakeUOW


async def test_login():
    uow = FakeUOW()
    request_dict = {'email': '<EMAIL>', 'password': '<PASSWORD>'}
    await register(email=request_dict['email'], password=request_dict['password'], uow=uow)
    assert await login(request_dict['email'], request_dict['password'],uow) is True
    assert await login(email=request_dict['email'], password='aboba',uow=uow) is False