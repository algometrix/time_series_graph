from db import get_data_from_influx, get_measurements_from_influx
import json

def get_graph_data(**kwargs):
    name = kwargs['name']
    time = kwargs.get('time', None)
    return list(get_data_from_influx(name,time))[0]

def get_all_tables():
    return list(get_measurements_from_influx())[0]