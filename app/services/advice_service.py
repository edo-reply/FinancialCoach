from services import user_service, transaction_service

def get_advices(user_id: str):
    user = user_service.get_user(user_id)
    transactions = transaction_service.get_transactions(user_id)
    advice = {
        'advice': 'Riduci $'
    }
    return advice
