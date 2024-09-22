from src.domain.model import User
from src.logic.service import register, add_user, get_user_by_email
from src.uow.user.uow import FakeUOW


async def test_register():
    fake_uow = FakeUOW()
    assert await register(email='<EMAIL>', password='<PASSWORD>', uow=fake_uow) is True


async def test_add_user_and_get_by_email():
    user = User(email='<EMAIL>', password='<PASSWORD>')
    fake_uow = FakeUOW()
    await add_user(uow=fake_uow, email=user.email, password=user.password)
    assert fake_uow.committed is True

    expected_email = await get_user_by_email(user.email,uow=fake_uow)
    assert expected_email.email == user.email
