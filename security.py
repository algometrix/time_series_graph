from werkzeug.security import safe_str_cmp




def identity(payload):
    user_id = payload['idenitity']
    print(user_id)
    return None


