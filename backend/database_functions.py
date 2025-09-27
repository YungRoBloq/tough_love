#imports
import sqlite3
from datetime import datetime

#Global Variables
CONN = sqlite3.Connection("../database/sensor_data.db")
CUR = CONN.cursor()

#Functions

#Write UV Data
def write_uv_data(data: dict):
    uv_index = data["uv_index"]
    timestamp = datetime.now()