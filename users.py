import db
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def save_user(self):
        db.save_user(self.username, self.password)

    