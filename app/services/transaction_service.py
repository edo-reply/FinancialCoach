from sqlite3 import IntegrityError

from models.transaction import UserTransaction
from db import Repository
from smartagent import engine

transaction_repo = Repository(UserTransaction)


def get_transactions(user_id: str) -> list[UserTransaction] | None:
    result = transaction_repo.select(user_id=user_id)
    if result:
        return result
    else:
        return None


def create_transactions(transaction: UserTransaction) -> UserTransaction | None:
    try:
        transaction.rating = engine.rate_transaction(transaction)
        transaction_repo.insert(transaction)
    except IntegrityError as err:
        print(err)
        return None
    return transaction
