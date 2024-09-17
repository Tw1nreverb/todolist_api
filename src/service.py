import bcrypt
from pydantic import BaseModel


def get_hashed_password(password: str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class TaskDTO(BaseModel):
    id: int
    name: str
    date_start: str
    date_end: str
