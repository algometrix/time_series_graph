from flask import Flask, render_template, request, Response, jsonify
from flask_restful import Resource, Api
from graph import get_graph_data, get_all_tables, save_user_graph
from users import User, UsersRegister
from security import authenticate, identity
from flask_jwt import JWT, jwt_required, current_identity

app = Flask(__name__)
app.secret_key = 'change_it_later'
api = Api(app)

jwt =  JWT(app, authenticate, identity)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods = ['GET','POST'] )
def login():
    if request.method == 'GET':
        return render_template("login.html")

@app.route("/sign_up", methods = ['GET','POST'] )
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    elif request.method == 'POST':
        data = request.form
        username = data['email']
        password = data['password']
        user = User(username, password)
        user.save_user()

@app.route('/dashboard', methods = ['GET','POST'])
def dashboard():
    if request.method == 'GET':
        return render_template('dashboard.html')
    elif request.method == 'POST':
        pass

class GraphData(Resource):
    @jwt_required()
    def get(self, name):
        print("Requested by " + str(current_identity))
        print(str(current_identity.id))
        return jsonify(get_graph_data(name=name))
        
class Items(Resource):
    def get(self):
        return jsonify(get_all_tables())

class MappedGraphs(Resource):
    
    @jwt_required()
    def get(self):
        measurements = get_all_tables()
        return jsonify(measurements)
    @jwt_required()
    def post(self):
        current_user_id = current_identity.id
        data = request.get_json(silent=True)
        graph_name = data['graph_name']
        measurements = data['measurements']
        print(graph_name)
        print(measurements)
        save_user_graph(current_user_id, save_user_graph, measurements)

api.add_resource(GraphData, '/graph_data/<string:name>')
api.add_resource(UsersRegister, '/user_create')
api.add_resource(Items, '/get_all_tables')
api.add_resource(MappedGraphs, '/mapped_graphs')

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)