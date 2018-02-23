from db import get_data_from_influx, get_measurements_from_influx, save_graph_for_user, save_measurements_for_user, get_user_graphs_from_db
import json

def get_graph_data(**kwargs):
    name = kwargs['name']
    time = kwargs.get('time', None)
    return {'name' : name, 'values' : list(get_data_from_influx(name,time))[0] }

def get_all_tables():
    return list(get_measurements_from_influx())[0]

def save_user_graph(user_id, graph_name, measurements):
    """Save user graphs to database
    
    Arguments:
        user_id {integer} -- [description]
        graph_name {text} -- [description]
        measurements {list} -- [description]
    """
    graph_id = save_graph_for_user(int(user_id), graph_name)
    for item in measurements:
        save_measurements_for_user(int(graph_id), item)

def get_user_graphs(user_id):
    graphs = get_user_graphs_from_db(user_id)
    return list(graphs)