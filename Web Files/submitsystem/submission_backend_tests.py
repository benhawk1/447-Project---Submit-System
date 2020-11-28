from submission_backend import * #get functions from submission_backend.py
from section_management import *
from submitsystem.db_func import *
import time


###################
###Constants
###################

ASSIGNMENT_ID = "hello_world"
FILENAME_TEST = "test files\hello_world.py"
COLLECTION_NAME = "CMSC 201"
STUDENT_ID = "12345"
STUDENT_NAME = "Queen Victoria"
SECTION_NUM = 5
DUE_DATE = "2020-10-31 23:59" #change appropriately to test "late submission" messages


if __name__ == "__main__":

    add_section(SECTION_NUM, COLLECTION_NAME)

    add_student(STUDENT_ID, STUDENT_NAME, SECTION_NUM, COLLECTION_NAME)

    add_assignment(SECTION_NUM, ASSIGNMENT_ID, FILENAME_TEST, DUE_DATE, COLLECTION_NAME)

    list_collection(COLLECTION_NAME) #should now have one student and one assignment
    
    ret_val = submit_file(STUDENT_ID, ASSIGNMENT_ID, SECTION_NUM, FILENAME_TEST, COLLECTION_NAME)
    print("This should be 0: ", ret_val)

    list_collection(COLLECTION_NAME) #should now have submission in Victoria's submissions list

    #add 3 more submissions and get most recent
    print("Adding 3 more submissions...\n")
    for i in range(3):
        time.sleep(5) #wait 5 seconds
        submit_file(STUDENT_ID, ASSIGNMENT_ID, SECTION_NUM, FILENAME_TEST, COLLECTION_NAME)
        print("submission made at ", time.ctime())

    #should now have 4 submissions
    list_collection(COLLECTION_NAME)

    print()
    latest_sub = get_latest_submission(STUDENT_ID, SECTION_NUM, COLLECTION_NAME)
    print("Latest submission from " + STUDENT_NAME + " in " + COLLECTION_NAME + ", section" , SECTION_NUM  , " is: " , latest_sub)

    drop_collection(COLLECTION_NAME)

    

    
