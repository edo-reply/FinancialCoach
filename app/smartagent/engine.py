from random import random
from math import floor

from models.transaction import Transaction

def rate_transaction(transaction: Transaction):
    return floor(random() * 10)
