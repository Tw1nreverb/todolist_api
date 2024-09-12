import bcrypt
def get_hashed_password(password: str):
    return bcrypt.hashpw(password.encode(),bcrypt.gensalt())
