from random import random

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

from models import Transaction

def rate_transaction(transaction: Transaction):
    return random() * 4


def cut_transactions(transactions: list[Transaction], budget: float) -> list[Transaction]:
    ratings = np.fromiter((t.rating for t in transactions), float)
    costs = np.fromiter((t.amount for t in transactions), float)
    bounds = Bounds(0, 1)
    integrality = np.full_like(ratings, True)
    constraints = LinearConstraint(A=costs, lb=0, ub=budget)

    res = milp(c=-ratings, constraints=constraints, integrality=integrality, bounds=bounds)

    return [t for i, t in enumerate(transactions) if res.x[i] < 1]
