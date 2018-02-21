from werkzeug.security import safe_str_cmp
from db import user_exists
def check_user(username, password):
    pass

def authenticate(username, password):
    if user_exists(username, password):
        return True
    else:
        return False

def identity(payload):
    print("Checking identity.")
    print(payload)
    user_id = payload['idenitity']
    print("==========================")
    print(user_id)
    return None


