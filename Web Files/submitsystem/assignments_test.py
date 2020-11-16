from assignments import *
import pandas as pd

#test datetime function

MONTH = "12"
DAY = "31"
YEAR = "2021"
HOUR = "23"
MINUTE = "59"


#should print out Date in YYYY-MM-DD format, then
#Time in HH:MM:SS format, then both combined
duedate_to_datetime(MONTH, DAY, YEAR, HOUR, MINUTE)



loginInfo = pd.read_csv("C:/Users/benha/Documents/CMSC 447 Project/Users.csv")

# This program will test the usage of the functions within assignments.py. Once this function runs, it will ask for the
# user to give one of the listed courses. If it is incorrect, it will prompt them again. If it is correct, it will then
# ask for a section number or 'All'. If the incorrect value is given, it will reprompt. Otherwise, it will ask for a
# name for the new assignment, and then a date and time for the assignment. If the values given for the date and time
# are invalid, then the user will be reprompted accordingly.
addAssignment(0, loginInfo)



