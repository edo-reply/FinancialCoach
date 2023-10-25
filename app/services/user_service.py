def get_user(user_id):
    print("get user: ", user_id)
    return {"name":"Mario", "surname": "Rossi"}

def create_user(data):
    print("create user: ", data)
    return {"name":"Mario", "surname": "Rossi"}

def delete_user(user_id):
    print("delete user: ", user_id)
    return True
