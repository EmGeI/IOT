#!/usr/bin/python3
# coding: utf-8

from influxdb import InfluxDBClient
import json
import dateutil.parser
from babel import Locale
from babel.dates import format_date, format_datetime, format_time

# Babel settings

# InfluxDB connections settings
host = '10.10.3.56'
port = 8086
user = ''
password = ''
dbname = 'letterbox'

client = InfluxDBClient(host, port, user, password, dbname)
query = 'SELECT * FROM "letterbox"."autogen"."delivery" WHERE time > now() - 24h ORDER BY time DESC LIMIT 1;'

result = client.query(query)

datas = result.get_points()
for data in datas:
    #print("Time: %s, value: %s" % (data['time'], data['value']))
    date = data['time']
    dt = dateutil.parser.parse(date)
    #print(dt)
    day = format_datetime(dt, "dd", locale="fr")
    month = format_datetime(dt, "MMMM", locale="fr")
    year = format_datetime(dt, "YYYY", locale="fr")
    hour = format_datetime(dt, "HH", locale="fr")
    minute = format_datetime(dt, "MM", locale="fr")

    print("Le facteur est passé le ", day, month, year, "à ", hour, "h",minute)
