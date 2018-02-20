from influxdb import InfluxDBClient
import sqlite3

def get_data_from_influx(name, time = None):
    client = InfluxDBClient(database='app_db')
    if time is not None:
        query_statement = 'select value from %s where time > %s' % (name, time)
    else:
        query_statement = 'select value from %s' % (name)
    
    result = client.query(query_statement)
    client.close()
    return result

def run_query_sqlite(query):
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute(query)
    conn.close()
    return c

def save_user(username, password):
    data = (username, password)
    run_query_sqlite('insert into users(username, password) values(%s,%s)' % data )

def check_user(username, password):
    pass