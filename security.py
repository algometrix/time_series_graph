from werkzeug.security import safe_str_cmp
from db import user_exists, get_user
from users import User
def check_user(username, password):
    pass

def authenticate(username, password):
    user = get_user(username, password)
    return User(user[0],password,id=user[1])

def identity(payload):
    print("Checking identity.")
    print(payload)
    user_id = payload['idenitity']
    print("==========================")
    print(user_id)
    return None


