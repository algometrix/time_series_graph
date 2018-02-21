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

def run_query_sqlite(query, *args):
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute(query, args)
    conn.commit()
    conn.close()
    return c

def save_user(username, password):
    run_query_sqlite("insert into users(username, password) values(?,?)" , username, password)

def user_exists(username, password):
    query = "select username from users where username=? and password=?"
    result = run_query_sqlite(query, username, password)
    if result.fetchone() is not None:
        return True
    else:
        return False