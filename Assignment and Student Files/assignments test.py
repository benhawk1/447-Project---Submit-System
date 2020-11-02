import assignments
import pandas as pd
loginInfo = pd.read_csv("C:/Users/benha/Documents/CMSC 447 Project/Users.csv")

# This program will test the usage of the functions within assignments.py. Once this function runs, it will ask for the
# user to give one of the listed courses. If it is incorrect, it will prompt them again. If it is correct, it will then
# ask for a section number or 'All'. If the incorrect value is given, it will reprompt. Otherwise, it will ask for a
# name for the new assignment, and then a date and time for the assignment. If the values given for the date and time
# are invalid, then the user will be reprompted accordingly.
assignments.addAssignment(0, loginInfo)


