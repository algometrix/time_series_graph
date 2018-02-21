import db
from flask_restful import Resource, Api, reqparse
from flask import request

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def save_user(self):
        db.save_user(self.username, self.password)

class UsersRegister(Resource):
    args = reqparse.RequestParser()
    args.add_argument('username')
    args.add_argument('password')
    def post(self):
        data = request.form   
        print(data)
        return {'data':data}



    