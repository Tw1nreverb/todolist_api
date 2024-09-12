from src.model import User
from src.service import get_hashed_password
import bcrypt
def test_user_hash_password():
    user = User(
        name='Vlad',
        password='qwerty123',
        email='index@mail.ru',
    )
    user_hashed_password = get_hashed_password(user.get_password())
    assert bcrypt.checkpw(user.get_password().encode(),user_hashed_password)
