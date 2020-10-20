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

FILENAME_TEST = "help.txt"
COLLECTION_NAME = "student_submissions"



    


if __name__ == "__main__":

    
    return_obj = submit_file(FILENAME_TEST, COLLECTION_NAME)
    print("This should print True: ", return_obj.acknowledged)
    print("bson ObjectID: ", return_obj.inserted_id)

    list_collection(COLLECTION_NAME)    

    #clean up collection for testing if needed
    #drop_collection(COLLECTION_NAME)

    

    
