import db
from flask_restful import Resource, Api, reqparse
from flask import request


parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')


class User:
    def __init__(self, username, password, id = None):
        self.id = id # Needed for Flask JWT
        self.username = username
        self.password = password
    
    def save_user(self):
        db.save_user(self.username, self.password)

class UsersRegister(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        username = args.get('username', None)
        password = args.get('password', None)
        print(username)
        print(password)
        user = User(username, password)
        user.save_user()
        return {'message':'User Created'},201