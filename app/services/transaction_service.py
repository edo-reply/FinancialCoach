from typing import Sequence
from sqlalchemy import select

from models import Transaction, get_fields
from database import db
from smartagent import engine


def get_transactions(user_id: str) -> Sequence[Transaction] | None:
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
    except Exception as err:
        print(err)
        return None
    return transaction

def update_transactions(transaction: Transaction) -> Transaction | None:
    try:
        fields = get_fields(transaction)
        db.session.query(Transaction) \
            .filter_by(id=transaction.id, user_id=transaction.user_id) \
            .update(fields)
        db.session.commit()
    except Exception as err:
        print(err)
        return None
    return transaction
