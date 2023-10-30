from models.user import User
from db import Repository

user_repo = Repository(User)


def get_user(user_id: str) -> User:
    result = user_repo.select(id=user_id)
    if result:
        return result[0]
    else:
        return None


def create_user(user: User) -> User:
    user_repo.insert(user)
    return user


def delete_user(user_id: str) -> bool:
    user_repo.delete(id=user_id)
    return True
