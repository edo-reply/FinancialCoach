from random import random
from math import floor

from app.models.transaction import UserTransaction

def rate_transaction(transaction: UserTransaction):
    return floor(random() * 10)
