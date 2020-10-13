import pymongo
import base64
import bson
import pytz
from bson.binary import Binary
from datetime import datetime, timezone

#####################
###Constants
#####################
MONGODB_URL = ""
PORT_NUM = 27017
TIMEZONE = "US/Eastern"

#####################

def get_timestamp():
    #first get UTC time, then convert to EST to avoid issues with daylight savings
    utc = pytz.timezone("UTC")
    now = utc.localize(datetime.utcnow())
    
    tz = pytz.timezone(TIMEZONE)
    local_time = now.astimezone(tz)
    
    print("now =", local_time)
    dt_string = local_time.strftime("%m/%d/%Y %H:%M:%S")
    print("date and time =" , dt_string)
    return dt_string

def submit_file(filename):
    #attempt database connection
    try:
        client = pymongo.MongoClient(MONGODB_URL, PORT_NUM)
        print("Connection successful")
    except:
        print("Connection failed")
        
    db = client.admin
    server_status = db.command("serverStatus")
    pprint(server_status)

    collection = db.student_submissions
    with open(filename, 'r') as f:
        encoded = Binary(f.read())
        time_string = get_timestamp()
        #insert document into db; structure depends on structure of database
        collection.insert({"filename": filename, "file": encoded, "description": "test", "time": time_string})

    f.close()

get_timestamp()
    
    
    
