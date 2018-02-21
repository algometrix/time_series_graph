from flask import Flask, render_template, request
from flask_restful import Resource, Api
from graph import get_graph_data
from users import User, UsersRegister
app = Flask(__name__)
api = Api(app)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods = ['GET','POST'] )
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        data = request.form
        username = data['email']
        password = data['password']

@app.route("/signup", methods = ['GET','POST'] )
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    elif request.method == 'POST':
        data = request.form
        username = data['email']
        password = data['password']
        user = User(username, password)
        user.save_user()

class GraphData(Resource):
    def get(self, name):
        return get_graph_data(name=name)           

api.add_resource(GraphData, '/graph_data/<string:name>')
api.add_resource(UsersRegister, '/test')

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)