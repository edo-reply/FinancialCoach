from datetime import date

from services import user_service, transaction_service
from smartagent.engine import cut_transactions
from models import RatingClass


def get_insights(user_id: str) -> dict | None:
    user = user_service.get_user(user_id)
    if user is None:
        return None

    all_transactions = transaction_service.get_transactions(user_id)
    if all_transactions is None:
        return None

    # Base insight model
    insights = {"messages": []}

    # Get transactions for this month
    today = date.today()
    transactions = [t for t in all_transactions 
                         if t.created_on is not None
                            and t.created_on.year == today.year
                            and t.created_on.month == today.month]

    # Total budget for the month, defined from the user
    if user.budget is None or user.budget == 0:
        insights['messages'].append('The current budget is not set, cannot get insights')
        return insights
    total_budget = user.budget

    # Remove all NEED transactions cost, and check if we have enough
    total_budget -= sum(t.amount for t in transactions if RatingClass.Need.eq(t.rating) and t.amount is not None)
    if total_budget <= 0:
        insights['messages'].append('Too many NEED transactions for the month, cannot calculate insights')
        return insights # TODO add something else?

    # Calculate transactions to be cut through the smartagent engine
    not_need_transactions = [t for t in transactions if not RatingClass.Need.eq(t.rating)]
    examples = cut_transactions(not_need_transactions, total_budget)

    if examples:
        insights['examples'] = examples
        
        insights['message'].append('You should cut some costs')
    else:
        insights['message'].append('Good job! everything is under budget')

    return insights
