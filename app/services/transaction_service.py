from sqlite3 import IntegrityError

from models.transaction import UserTransaction
from db import Repository

transaction_repo = Repository(UserTransaction)


def get_transactions(user_id: str) -> UserTransaction:
    result = transaction_repo.select(user_id=user_id)
    if result:
        return result
    else:
        return None


def create_transactions(transaction: UserTransaction) -> UserTransaction:
    try:
        transaction_repo.insert(transaction)
    except IntegrityError as err:
        print(err)
        return None
    return transaction
