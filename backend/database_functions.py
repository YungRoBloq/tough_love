#imports
import sqlite3
from datetime import datetime, timedelta

#Global Variables
CONN = sqlite3.Connection("../database/sensor_data.db")
CUR = CONN.cursor()

#Functions

#Write UV Data
def write_uv_data(data: dict) -> tuple:
    sensor_id = data["sensor_id"]
    uv_index = data["value"]
    timestamp = datetime.now()

    add_sql = "INSERT INTO UV_Data (sensor_id, uv_index, time_stamp) VALUES (?, ?, ?)"
    values = (sensor_id, uv_index, timestamp)

    try:
        CUR.execute(add_sql, values)
        CONN.commit()

        return(True, )
    
    except Exception as e:
        return(False, e)

#Write AQ Data
def write_aq_data(data:dict) -> tuple:
    sensor_id = data["sensor_id"]
    aq_index = data["value"]
    timestamp = datetime.now()

    add_sql = "INSERT INTO AQ_Data (sensor_id, aq_index, time_stamp) VALUES (?, ?, ?)"
    values = (sensor_id, aq_index, timestamp)

    try:
        CUR.execute(add_sql, values)
        CONN.commit()

        return (True, )
    except Exception as e:
        return(False, e)

#Read latest aq data
def read_aq_data() -> dict:
    query = "SELECT * FROM AQ_Data WHERE reading_id = (SELECT MAX(reading_id) FROM AQ_Data)"
    latest_aq_data = CUR.execute(query).fetchall()[0]

    structure = {
        "sensor_id": latest_aq_data[1],
        "value": latest_aq_data[2],
        "timestamp": latest_aq_data[3]
    }

    return structure

def read_uv_data() -> dict:
    query = "SELECT * FROM UV_Data WHERE reading_id = (SELECT MAX(reading_id) FROM UV_Data)"
    latest_uv_data = CUR.execute(query).fetchall()[0]

    structure = {
        "sensor_id": latest_uv_data[1],
        "value": latest_uv_data[2],
        "timestamp": latest_uv_data[3]
    }

    return structure


#Determing if allowed to send notification
#This is to make sure that the user is not notified to frequently
def can_send_noti() -> tuple:
    min_wait = timedelta(seconds=5)

    latest_noti_query = "SELECT timestamp FROM notification WHERE notification_id = (SELECT MAX(notification_id) FROM notification)"
    latest_noti = CUR.execute(latest_noti_query).fetchall()

    if len(latest_noti) > 0:
        latest_timestamp_str = latest_noti[0][0]
        DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'

        latest_datetime = datetime.strptime(latest_timestamp_str, DATE_FORMAT)
        time_difference = datetime.now() - latest_datetime

        if time_difference > min_wait:
            return(True, )
        else:
            return(False, time_difference)
    else:
        return (True, )

#Add log of notification
def write_notification():
    pass


read_aq_data()