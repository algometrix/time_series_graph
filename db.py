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