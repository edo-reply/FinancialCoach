from random import random
from math import floor
from typing import Iterable
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from time import time

from models import Transaction

def rate_transaction(transaction: Transaction):
    return random() * 4


def cut_transactions(transactions: Iterable[Transaction], budget: float) -> list[Transaction]:
    start = time()

    costs = np.array((t.amount for t in transactions))
    ratings = np.array((t.rating for t in transactions))
    bounds = Bounds(0, 1)
    integrality = np.full_like(ratings, True)
    constraints = LinearConstraint(A=costs, lb=0, ub=budget)

    print('start milp')
    print('costs', costs)
    print('ratings', ratings)

    res = milp(c=-ratings, constraints=constraints, integrality=integrality, bounds=bounds)
    print('elapsed', time() - start)
    return [t for i, t in enumerate(transactions) if res.x[i] > 0]
