from typing import Sequence
from sqlalchemy import select

from database import db
from models import Transaction, update_model
from smartagent.engine import rate_transaction


def get_transactions(user_id: str) -> Sequence[Transaction] | None:
    result = db.session.scalars(select(Transaction).filter_by(user_id = user_id)).all()
    if result:
        return result
    else:
        return None


def create_transactions(transaction: Transaction) -> Transaction | None:
    try:
        transaction.created_on = None
        transaction.rating = rate_transaction(transaction)
        db.session.add(transaction)
        db.session.commit()
    except Exception as err:
        print(err)
        return None
    return transaction

def update_transactions(transaction: Transaction) -> Transaction | None:
    try:
        transaction.created_on = None
        to_update = db.session.get(Transaction, transaction.id)
        update_model(to_update, transaction)
        db.session.commit()
    except Exception as err:
        print(err)
        return None
    return to_update
