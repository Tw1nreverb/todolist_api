from domain.model import User
from src.logic.hash import get_password_hash
import bcrypt
def test_user_hash_password():
    user = User(
        name='Vlad',
        password='qwerty123',
        email='index@mail.ru',
    )
    user_hashed_password = get_password_hash(user.get_password())
    assert bcrypt.checkpw(user.get_password().encode(),user_hashed_password)
