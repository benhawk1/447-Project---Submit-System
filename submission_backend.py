import pytz
import os
from bson.binary import Binary
from datetime import datetime
from db_func import *

#####################
###Constants
#####################
TIMEZONE = "US/Eastern"
MONGODB_URL = "mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb"
PORT_NUM = 27017

#####################

def submit_file(student_ID, section, filepath, coll_name):
    #connect to database, access collection
    client = connect_client()
    if client == -1:
        return -1
    
    db = connect_db(client)

    collection = connect_collection(db, coll_name)

    #iterate over section documents
    for doc in collection.find({}):
        if doc["section"] == section:
            #iterate over list of student dictionaries
            for i in range(len(doc["students"])):
                #if the ith student dict has a matching ID, we've found our student
                if doc["students"][i]["ID"] == student_ID:
                   #create and append submission dict to student's submissions 
                    submission_dict = {}
                    with open(filepath, 'rb') as f:
                        encoded = Binary(f.read())                    
                    f.close()

                    filename = os.path.basename(filepath)
                    time_string = get_timestamp()
                    submission_dict = {"filename" : filename,
                                       "file" : encoded ,
                                       "timestamp" : time_string}

                    new_doc = doc
                    new_doc["students"][i]["submissions"].append(submission_dict)

                    #first parameter is for identifying which doc to update
                    #second parameter is new document
                    #upsert parameter will insert if doc is not found in def
                    collection.update_one({"section": section}, {"$set" : new_doc}, upsert=False)
                    return 0
                
            print("student ID not found")
            return -1
    print("section not found")
    return -1
                    


def get_timestamp():
    #first get UTC time, then convert to EST to avoid issues with daylight savings
    utc = pytz.timezone("UTC")
    now = utc.localize(datetime.utcnow())
    
    tz = pytz.timezone(TIMEZONE)
    local_time = now.astimezone(tz)
    
    dt_string = local_time.strftime("%m/%d/%Y %H:%M:%S")
    return dt_string
