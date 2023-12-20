from services import user_service, transaction_service

def get_advices(user_id: str):
    user = user_service.get_user(user_id)
    transactions = transaction_service.get_transactions(user_id)
    user.budget
    need = [t for t in transactions ]
    advice = {
        'examples': transactions[0:3]
    }
    return advice
# € da risparmiare sulla restante parte della mensilità

# % budget da dedicare a una determinata classe (rating)
#NEED  70%
#LOVE  15%
#WANT  10%
#LIKE  5%
# se si sfora il budget per la classe con le attuali trx aggiungere ai suggerimenti di taglio con seguente logica:
#   ordinare trx in base a costo prenderne N tra quelle più costose in modo da portare il budget sotto il limite

# calcolo costo totale per categoria su trx calcolate sopra (da tagliare)
