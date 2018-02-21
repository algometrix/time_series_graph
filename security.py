from werkzeug.security import safe_str_cmp
from db import user_exists, get_user, get_user_by_username, get_user_by_id
from users import User
def check_user(username, password):
    pass

def fetch_user(username, password):
    user = get_user(username, password)
    return User(user[1],password,id=user[0])

def fetch_user_by_username(username):
    user = get_user_by_username(username)
    return User(user[1],None, user[0])

def fetch_user_by_id(user_id):
    user = get_user_by_id(user_id)
    return User(user[1],None, user[0])

def authenticate(username, password):
    return fetch_user(username,password)

def identity(payload):
    print("Checking identity.")
    print(payload)
    user_id = payload['identity']
    print("==========================")
    print(user_id)
    return fetch_user_by_id(user_id)


