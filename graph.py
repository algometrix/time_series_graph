from db import get_data_from_influx, get_measurements_from_influx
import json

def get_graph_data(**kwargs):
    name = kwargs['name']
    time = kwargs.get('time', None)
    return json.dumps(list(get_data_from_influx(name,time))[0])

def get_all_tables():
    return json.dumps( list(get_measurements_from_influx())[0] )