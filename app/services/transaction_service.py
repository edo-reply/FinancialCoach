from sqlite3 import IntegrityError

from sqlalchemy import select

from models import Transaction
from database import db
from smartagent import engine


def get_transactions(user_id: str) -> list[Transaction] | None:
    result = db.session.scalars(select(Transaction).filter_by(user_id = user_id)).all()
    if result:
        return result
    else:
        return None


def create_transactions(transaction: Transaction) -> Transaction | None:
    try:
        transaction.rating = engine.rate_transaction(transaction)
        db.session.add(transaction)
        db.session.commit()
    except IntegrityError as err:
        print(err)
        return None
    return transaction

def update_transactions(user_id: str, transaction_id: str, transaction: Transaction) -> Transaction | None:
    try:
        db.session.query(Transaction).filter(Transaction.id == transaction_id and Transaction.user_id == user_id).update({'rating': transaction.rating})
        db.session.commit()
    except IntegrityError as err:
        print(err)
        return None
    return transaction
