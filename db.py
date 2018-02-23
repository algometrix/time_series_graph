from influxdb import InfluxDBClient
import sqlite3

def get_data_from_influx(name, time = None):
    client = InfluxDBClient(database='app_db')
    if time is not None:
        query_statement = 'select time,value from %s where time > %s' % (name, time)
    else:
        query_statement = 'select time,value from %s' % (name)
    
    result = client.query(query_statement, epoch='ms')
    client.close()
    return result

def get_measurements_from_influx():
    client = InfluxDBClient(database='app_db')
    query_statement = 'show MEASUREMENTS;'
    result = client.query(query_statement)
    client.close()
    return result

def run_query_sqlite(query, *args):
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute(query, args)
    conn.commit()
    return c, conn

def save_user(username, password):
    run_query_sqlite("insert into users(username, password) values(?,?)" , username, password)

def user_exists(username, password):
    query = "select username from users where username=? and password=?"
    result, conn = run_query_sqlite(query, username, password)
    response = result.fetchone()
    conn.close()
    if response is not None:
        return True
    else:
        return False

def get_user(username, password):
    query = "select id,username from users where username=? and password=?"
    result, conn = run_query_sqlite(query, username, password)
    response = result.fetchone()
    conn.close()
    return response

def get_user_by_username(username):
    query = "select id,username from users where username=?"
    result, conn = run_query_sqlite(query, username)
    response = result.fetchone()
    conn.close()
    return response

def get_user_by_id(user_id):
    query = "select id,username from users where id=?"
    result, conn = run_query_sqlite(query, user_id)
    response = result.fetchone()
    conn.close()
    return response

def save_graph_for_user(user_id, graph_name):
    print("User:"+str(user_id))
    print("Graph:"+str(graph_name))
    run_query_sqlite("insert into user_graphs(user_id, graph_name) values(?,?)" , user_id, graph_name)
    query = "select id from user_graphs where user_id=? and graph_name=?"
    result, conn = run_query_sqlite(query, user_id, graph_name)
    response = result.fetchone()
    conn.close()
    return response[0]

def save_measurements_for_user(graph_id, measurement):
    print("graph_id:"+str(graph_id))
    print("measurement:"+str(measurement ))
    run_query_sqlite("insert into graph_measurements(graph_id, measurement) values(?,?)" , graph_id, measurement)
    query = "select id from graph_measurements where graph_id=? and measurement=?"
    result, conn = run_query_sqlite(query, graph_id, measurement)
    response = result.fetchone()
    conn.close()
    return response[0]

def get_user_graphs_from_db(user_id):
    query = "select id,graph_name from user_graphs where user_id=??"
    result, conn = run_query_sqlite(query, user_id)
    response = result.fetchone()
    conn.close()
    return response