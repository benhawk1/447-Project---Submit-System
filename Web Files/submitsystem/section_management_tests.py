from submitsystem.db_func import *
from section_management import *
#####################
###Constants
#####################
COURSE_NAME = "CMSC 447"
SECTION_NUM = 5
STUDENT_NAME = "Eric Hamilton"
NEW_NAME = "Heric Amilton"
STUDENT_ID = "EH999"
ASSIGNMENT_ID = "hw1"
ASSIGNMENT_FILEPATH = "test files\hw1.txt"
ASSIGNMENT_FILENAME = "hw1.txt"
DUE_DATE = "2020-12-31 23:59"
#####################

################
##Example of section document in collection:
##{_id: 3 , "students" : {"12345": "Abraham Lincoln", "MT3902": "Queen Victoria", "JC4958": "Plato"}}
##3 is section number; inner dict is student ID: student name
################

create_collection(COURSE_NAME)

add_section(SECTION_NUM,
            COURSE_NAME)

list_collection(COURSE_NAME) #empty section

add_student(STUDENT_ID, STUDENT_NAME, SECTION_NUM, COURSE_NAME)

list_collection(COURSE_NAME) #Eric is added to list of students

modify_student(STUDENT_ID, NEW_NAME, SECTION_NUM, COURSE_NAME)

list_collection(COURSE_NAME) #Eric's name is changed

remove_student(STUDENT_ID, SECTION_NUM, COURSE_NAME)

list_collection(COURSE_NAME) #Eric is removed

add_assignment(SECTION_NUM, ASSIGNMENT_ID, ASSIGNMENT_FILEPATH, DUE_DATE, COURSE_NAME)

list_collection(COURSE_NAME) #assignment is added

remove_assignment(SECTION_NUM, ASSIGNMENT_ID, COURSE_NAME)

list_collection(COURSE_NAME) #assignment is removed

drop_collection(COURSE_NAME)


