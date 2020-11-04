from submission_backend import * #get functions from submission_backend.py
from db_func import *
from section_management import *


###################
###Constants
###################

FILENAME_TEST = "Web Files/submitsystem/test files\hello_world.py"
COLLECTION_NAME = "sections_test"
STUDENT_ID = "12345"
STUDENT_NAME = "Queen Victoria"
SECTION_NUM = 5


if __name__ == "__main__":

    add_section(SECTION_NUM, COLLECTION_NAME)

    add_student(STUDENT_ID, STUDENT_NAME, SECTION_NUM, COLLECTION_NAME)

    list_collection(COLLECTION_NAME) #should now have one student
    
    ret_val = submit_file(STUDENT_ID, SECTION_NUM, FILENAME_TEST, COLLECTION_NAME)
    print("This should be 0: ", ret_val)

    list_collection(COLLECTION_NAME) #should now have submission in Victoria's submissions list

    drop_collection(COLLECTION_NAME)

    

    
