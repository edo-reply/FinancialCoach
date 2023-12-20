from sqlalchemy import delete, select
from models import User
from database import db


def get_user(user_id: str) -> User | None:
    result = db.session.scalar(select(User).filter_by(id=user_id))
    if result:
        return result
    else:
        return None


def create_user(user: User) -> User:
    db.session.add(user)
    db.session.commit()
    return user


def delete_user(user_id: str) -> bool:
    print(delete(User).filter_by(id=user_id))
    result = db.session.execute(delete(User).filter_by(id=user_id))
    db.session.commit()
    return result.rowcount == 1
