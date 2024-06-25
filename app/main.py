import clickhouse_connect
import sys
import json

CLICKHOUSE_CLOUD_HOSTNAME = 'clickhouse'
CLICKHOUSE_CLOUD_USER = 'username'
CLICKHOUSE_CLOUD_PASSWORD = 'password'

client = clickhouse_connect.get_client(
    host=CLICKHOUSE_CLOUD_HOSTNAME, port=8123, username=CLICKHOUSE_CLOUD_USER, password=CLICKHOUSE_CLOUD_PASSWORD)

print("connected to " + CLICKHOUSE_CLOUD_HOSTNAME + "\n")
client.command(
    'CREATE TABLE IF NOT EXISTS new_table (key UInt32, value String, metric Float64) ENGINE MergeTree ORDER BY key')

# print("table new_table created or exists already!\n")

# row1 = [1000, 'String Value 1000', 5.233]
# row2 = [2000, 'String Value 2000', -107.04]
# data = [row1, row2]
# client.insert('new_table', data, column_names=['key', 'value', 'metric'])

# print("written 2 rows to table new_table\n")

# QUERY = "SELECT max(key), avg(metric) FROM new_table"

# result = client.query(QUERY)

# sys.stdout.write("query: ["+QUERY + "] returns:\n\n")
# print(result.result_rows)