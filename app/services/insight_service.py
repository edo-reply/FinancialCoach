from collections import Counter
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

    # Get transactions for this month
    today = date.today()
    transactions = [t for t in all_transactions 
                         if t.created_on is not None
                            and t.created_on.year == today.year
                            and t.created_on.month == today.month]

    # Total budget for the month, defined from the user
    if user.budget is None or user.budget == 0:
        return {'messages': ['Cannot get insights because the current budget is not set. Please update your profile.']}
    total_budget = user.budget

    # Remove all NEED transactions cost, and check if we have enough
    total_budget -= sum(t.amount for t in transactions if RatingClass.Need.eq(t.rating) and t.amount is not None)
    if total_budget <= 0:
        return {'messages': ['Cannot get insights. Too many "NEED" transactions in this month.']}

    # Calculate transactions to be cut through the smartagent engine
    not_need_transactions = [t for t in transactions if not RatingClass.Need.eq(t.rating)]
    cut_examples = cut_transactions(not_need_transactions, total_budget)

    if cut_examples:
        messages = ['You should cut some costs.']

        # Check most common categories
        counter = Counter(t.category for t in cut_examples)
        common_categories = counter.most_common()
        if common_categories[0][1] - common_categories[1][1] > 1:
            category = common_categories[0][0] # TODO get textual category
            messages.append(f'Try reducing your expenses in the "{category}" category.')

        return {
            'messages': messages,
            'examples': cut_examples
        }

    return {'messages': ['Good job! everything is under budget.']}
