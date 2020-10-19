import pymongo
import base64
import bson
import pytz
import pprint
from bson.binary import Binary
from datetime import datetime, timezone

from submission_backend import * #get functions from submission_backend.py


###################
###Constants
###################
MONGODB_URL = "mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb"
PORT_NUM = 27017
FILENAME_TEST = "hello_world.py"
COLLECTION_NAME = "student_submissions"



    


if __name__ == "__main__":
    try:
        client = pymongo.MongoClient(MONGODB_URL, PORT_NUM)
        print("Connection successful")
    except:
        print("Connection failed")
        
    #access student_submissions database 
    db = client.student_submissions

    try:
        collection = client.db.create_collection(COLLECTION_NAME)
        print("Student Submission collection created")
    except:
        collection = db[COLLECTION_NAME]
        print("Student Submission collection already exists")

    return_obj = submit_file(collection, FILENAME_TEST)
    print("This should print True: ", return_obj.acknowledged)
    print("bson ObjectID: ", return_obj.inserted_id)
    
    cursor = collection.find({})
    for document in cursor:
        print(document)
