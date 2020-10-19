import pymongo
import base64
import bson
import pytz
from bson.binary import Binary
from datetime import datetime, timezone

#####################
###Constants
#####################
MONGODB_URL = "localhost"
PORT_NUM = 27017
TIMEZONE = "US/Eastern"

#####################

def get_timestamp():
    #first get UTC time, then convert to EST to avoid issues with daylight savings
    utc = pytz.timezone("UTC")
    now = utc.localize(datetime.utcnow())
    
    tz = pytz.timezone(TIMEZONE)
    local_time = now.astimezone(tz)

    dt_string = local_time.strftime("%m/%d/%Y %H:%M:%S")
    return dt_string

def submit_file(collection, filename):
    submission_dict = {}
    with open(filename, 'rb') as f:
        submission_dict["filename"] = filename

        encoded = Binary(f.read())
        submission_dict["file"] = encoded

        time_string = get_timestamp()
        submission_dict["timestamp"] = time_string

        submission_dict["description"] = "test"

    f.close()

    return collection.insert_one(submission_dict)




