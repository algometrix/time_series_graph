import db
from flask_restful import Resource, Api, reqparse
from flask import request

class User:
    def __init__(self, username, password, id = None):
        self.id = id # Needed for Flask JWT
        self.username = username
        self.password = password
    
    def save_user(self):
        db.save_user(self.username, self.password)

class UsersRegister(Resource):
    def post(self):
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)
        user = User(username, password)
        user.save_user()
        return {'message':'User Created'},201



    