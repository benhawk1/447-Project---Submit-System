import pymongo
import base64
import bson
import pytz
from bson.binary import Binary
from datetime import datetime, timezone

#####################
###Constants
#####################
TIMEZONE = "US/Eastern"
MONGODB_URL = "mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb"
PORT_NUM = 27017

#####################

def connect_client():
    try:
        client = pymongo.MongoClient('localhost')#MONGODB_URL, PORT_NUM)
        print("Client Connection successful")
        return client
    except:
        print("Client Connection failed")
        return -1;

def connect_db(client):
    db = client.student_submissions
    return db

def connect_collection(db, coll_name):
    try:
        collection = db[coll_name]
        print("Collection accessed")
    except:
        collection = client.db.create_collection(coll_name)
        print("Collection doesn't exist; new one created")

    return collection

def submit_file(filename, coll_name):
    #connect to database, access collection
    client = connect_client()
    if client == -1:
        return -1

    db = connect_db(client)

    collection = connect_collection(db, coll_name)

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

def list_collection(coll_name):
    client = connect_client()
    if client == -1:
        return -1

    db = connect_db(client)

    collection = connect_collection(db, coll_name)

    #print all documents in collection
    cursor = collection.find({})
    for document in cursor:
        print(document)

def drop_collection(coll_name):
    client = connect_client()
    if client == -1:
        return -1

    db = connect_db(client)

    collection = connect_collection(db, coll_name)

    collection.drop()


def get_timestamp():
    #first get UTC time, then convert to EST to avoid issues with daylight savings
    utc = pytz.timezone("UTC")
    now = utc.localize(datetime.utcnow())

    tz = pytz.timezone(TIMEZONE)
    local_time = now.astimezone(tz)

    dt_string = local_time.strftime("%m/%d/%Y %H:%M:%S")
    return dt_string
