from db import get_data_from_db
import json

def get_graph_data(**kwargs):
    name = kwargs['name']
    time = kwargs.get('time', None)
    return json.dumps(get_data_from_db(name,time))