from influxdb import InfluxDBClient

client = InfluxDBClient(database='app_db')

def get_data_from_db(name, time = None):
    if time is not None:
        query_statement = 'select value from %s where time > %s' % (name, time)
    else:
        query_statement = 'select value from %s' % (name)
    
    result = client.query(query_statement)
    return result
