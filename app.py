from flask import Flask, render_template, request
from flask_restful import Resource, Api
from graph import get_graph_data
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
        pass

class GraphData(Resource):
    def get(self, name):
        return get_graph_data(name=name)           

api.add_resource(GraphData, '/graph_data/<string:name>')

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)