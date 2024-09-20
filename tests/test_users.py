from domain.model import User
from src.logic.hash import get_password_hash, verify_password
def test_user_hash_password():
    user = User(
        password='qwerty123',
        email='index@mail.ru',
    )
    hashed_password = get_password_hash(user.password)
    assert verify_password(user.password,hashed_password) 
