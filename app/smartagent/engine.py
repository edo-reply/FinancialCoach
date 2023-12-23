import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

from models import Transaction
from smartagent.preprocess import load_features
from smartagent.data import model



def rate_transaction(transaction: Transaction) -> float:
    x = load_features(transaction)
    prediction = model.predict(x)
    return prediction[0]


def cut_transactions(transactions: list[Transaction], budget: float) -> list[Transaction]:
    ratings = np.fromiter((t.rating for t in transactions), float)
    costs = np.fromiter((t.amount for t in transactions), float)
    bounds = Bounds(0, 1)
    integrality = np.full_like(ratings, True)
    constraints = LinearConstraint(A=costs, lb=0, ub=budget)

    res = milp(c=-ratings, constraints=constraints, integrality=integrality, bounds=bounds)

    return [t for i, t in enumerate(transactions) if res.x[i] < 1]
