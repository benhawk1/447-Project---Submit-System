from submission_backend import * #get functions from submission_backend.py
from section_management import *
from submitsystem.db_func import *
import time


###################
###Constants
###################

COURSE_NAME = "CMSC 201"
SECTION_NUM = 5
STUDENT_NAME = "Queen Victoria"
STUDENT_ID = "12345"
ASSIGNMENT_ID1 = "hw1"
ASSIGNMENT_ID2 = "hw2"
ASSIGNMENT_FILEPATH = "test files\hw1.txt"
ASSIGNMENT_FILENAME = "hw1.txt"
SUBMISSION_FILEPATH = "test files\hello_world.py"
GOOD_DUE_DATE = "2028-10-31 23:59" #tests "on time" submission
BAD_DUE_DATE = "2008-08-31 10:00" #test "late" submission


if __name__ == "__main__":

    add_section(SECTION_NUM, COURSE_NAME)

    add_student(STUDENT_ID, STUDENT_NAME, SECTION_NUM, COURSE_NAME)

    add_assignment(SECTION_NUM, ASSIGNMENT_ID1, ASSIGNMENT_FILEPATH, GOOD_DUE_DATE, COURSE_NAME)

    list_collection(COURSE_NAME) #should now have one student and one assignment
    
    ret_val = submit_file(STUDENT_ID, ASSIGNMENT_ID1, SECTION_NUM, SUBMISSION_FILEPATH, COURSE_NAME)
    print("This should be 0: ", ret_val)

    list_collection(COURSE_NAME) #should now have submission in Victoria's submissions list

    #add 3 more submissions and get most recent
    print("Adding 3 more submissions...\n")
    for i in range(3):
        time.sleep(5) #wait 5 seconds
        submit_file(STUDENT_ID, ASSIGNMENT_ID1, SECTION_NUM, SUBMISSION_FILEPATH, COURSE_NAME)
        print("submission made at ", time.ctime())

    #should now have 4 submissions
    list_collection(COURSE_NAME)

    print()
    latest_sub = get_latest_submission(STUDENT_ID, SECTION_NUM, COURSE_NAME)
    print("Latest submission from " + STUDENT_NAME + " in " + COURSE_NAME + ", section" , SECTION_NUM  , " is: " , latest_sub)
    
    #test late submission, should print appropriate message after submit_file
    add_assignment(SECTION_NUM, ASSIGNMENT_ID2, ASSIGNMENT_FILEPATH, BAD_DUE_DATE, COURSE_NAME)
    
    submit_file(STUDENT_ID, ASSIGNMENT_ID2, SECTION_NUM, SUBMISSION_FILEPATH, COURSE_NAME)
    
    #should now have 5 submissions, 2 assignments
    list_collection(COURSE_NAME)

    drop_collection(COURSE_NAME)

    

    
