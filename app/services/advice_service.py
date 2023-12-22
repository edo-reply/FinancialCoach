from datetime import date

from services import user_service, transaction_service
from models import RatingClass
from smartagent.engine import cut_transactions


def get_advices(user_id: str) -> dict | None:
    user = user_service.get_user(user_id)
    if user is None:
        return None

    all_transactions = transaction_service.get_transactions(user_id)
    if all_transactions is None:
        return None

    # Base advice model
    advice = {"messages": []}

    # Get transactions for this month
    today = date.today()
    transactions = (t for t in all_transactions 
                         if t.created_on is not None
                            and t.created_on.year == today.year
                            and t.created_on.month == today.month)

    # Total budget for the month, defined from the user
    if user.budget is None or user.budget == 0:
        advice['messages'].append('The current budget is not set, cannot get advices')
        return advice
    total_budget = user.budget

    # Remove all NEED transactions cost, and check if we have enough
    need_transactions = filter(lambda t : RatingClass.Need.eq(t.rating), transactions)
    total_need = sum(t.amount for t in need_transactions if t.amount is not None)
    total_budget -= total_need
    if total_budget <= 0:
        advice['messages'].append('Too many NEED transactions for the month, cannot calculate advices')
        return advice # TODO add something else?


    # Calculate transactions to be cut through the smartagent engine
    not_need_transactions = filter(lambda t : not RatingClass.Need.eq(t.rating), transactions)
    advice['examples'] = cut_transactions(not_need_transactions, total_budget)

    return advice
