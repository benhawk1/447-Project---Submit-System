import pandas as pd
import datetime
from section_management import *

# Obtains a specified class, section(s), due date, due time, and name for a given assignment, for it to then be passed
# To the database as needed.
def addAssignment(row, df):
    # Obtains information for eligible classes and sections re assignment creation
    classes = str(df.at[row, 'Classes'])
    sections = str(df.at[row, 'Sections'])
    classes = list(classes.split(","))
    sections = list(sections.split(","))


   
    
    maxCount = len(classes)

    # Obtains a list of all unique classes taught by the current user
    myClasses = list(set(classes))
    myClassesCount = len(myClasses)

    # Prints possible classes, and obtains a class for assignment creation
    print("The list of potential classes for assignment creation are as follows:")
    for i in range(myClassesCount):
        print(myClasses[i])
    chosenClass = input("Please enter the class for your new assignment: ")
    while chosenClass not in classes:
        chosenClass = input("Invalid class. Please enter a valid class: ")

    # Prints possible sections, and obtains the section (or all) for assignment creation
    eligibleSections = []
    print("The list of sections for " + chosenClass + " are as follows:")
    count = 0
    for i in range(maxCount):
        if chosenClass == classes[i]:
            print(sections[i])
            eligibleSections.append(sections[i])
            count = count + 1
    chosenSection = input("Please enter a section number or \'All\': ")
    print(eligibleSections)
    while (chosenSection not in eligibleSections) and (chosenSection != "All"):
        chosenSection = input("Invalid section choice. Please enter a valid section: ")

    #Gets a name for the desired assignment
    assignmentName = input("Please enter the name of the assignment for course " + chosenClass
                           + " section " + chosenSection + ": ")

    # Asks for an initial input of a due date and time for the assignment
    dueDate = input("Please enter the due date for your assignment in the format \'MM-DD-YYYY\': ")
    dueTime = input("Please enter the assignment due time in the format \'HH:MM\' (in military time): ")
    dueDate = list(dueDate.split("-"))
    dueTime = list(dueTime.split(":"))
    checkDate = dueDateValidation(dueDate)
    checkTime = dueTimeValidation(dueTime)

    # Ensures that the users enter an appropriate due date
    while checkDate != 0:
        print("Invalid due date provided.")
        dueDate = input("Please enter the due date for your assignment in the format \'MM-DD-YYYY\': ")
        dueDate = list(dueDate.split("-"))
        checkDate = dueDateValidation(dueDate)

    # Ensures that the users enter an appropriate due time
    while checkTime != 0:
        print("Invalid due time provided.")
        dueTime = input("Please enter the assignment due time in the format \'HH:MM\' (in military time): ")
        dueTime = list(dueTime.split(":"))
        checkTime = dueTimeValidation(dueTime)

    # Assigns the values once they are validated
    Month = dueDate[0]
    Day = dueDate[1]
    Year = dueDate[2]
    Hour = dueTime[0]
    Minute = dueTime[1]

    # Prints out the provided information (will be replaced with a function call to enter the information)
    print("Assignment: " + assignmentName)
    print("Date: " + Month + "-" + Day + "-" + Year)
    print("Time: " + Hour + ":" + Minute)

    #convert duedate strings to single datetime object
    datetime = duedate_to_datetime(Month, Day, Year, Hour, Minute)

    #function call from section_management
    ret_val = add_assignment(chosenSection, assignmentName, datetime, chosenClass)
    if ret_val < 0:
        print("Error occurred: add_assignment")
    


# Ensures that the date given meets the proper requirements
def dueDateValidation(dueDate):
    # Ensures that there is the proper number of values, and all are numbers
    if len(dueDate) != 3:
        return -1
    if str.isdigit(dueDate[0]) is False or str.isdigit(dueDate[1]) is False or str.isdigit(dueDate[2]) is False:
        return -2

    # Ensures that the month given is valid
    if int(dueDate[0]) not in range(1, 13):
        return -3

    # Ensures that the date provided is valid
    if int(dueDate[0]) in (1, 3, 5, 8, 10, 12):
        if int(dueDate[1]) not in range(1, 32):
            return -4
    if int(dueDate[0]) in (4, 6, 7, 9, 11):
        if int(dueDate[1]) not in range(1, 31):
            return -5
    if int(dueDate[0]) == 2:
        if int(dueDate[1]) not in range(1, 30):
            return -6

    # Ensures that the year provided is valid
    if int(dueDate[2]) < 2020:
        return -7
    return 0


# Ensures that the time entered meets the proper criteria
def dueTimeValidation(dueTime):
    # Checks if two values were given
    if len(dueTime) != 2:
        return -1
    # Checks if the values given were numbers
    if str.isdigit(dueTime[0]) is False or str.isdigit(dueTime[1]) is False:
        return -2
    # Checks if the hour value given was within 0-23
    if int(dueTime[0]) not in range(0, 24):
        return -3
    # Checks if the minute value given was within 0-59
    if int(dueTime[1]) not in range(0, 60):
        return -4
    return 0

# Converts string of date and time to datetime object for easier use in future
def duedate_to_datetime(Month, Day, Year, Hour, Minute):
    #prepare string for conversion to datetime
    duedate_str = str(Year) + "-" + str(Month) + "-" + str(Day) + " " + str(Hour) + ":" + str(Minute)

    #format input string into datetime object
    date_time_obj = datetime.datetime.strptime(duedate_str, '%Y-%m-%d %H:%M')


    print("date time object test: ")
    print('Date:', date_time_obj.date())
    print('Time:', date_time_obj.time())
    print('Date-time:', date_time_obj)

    return date_time_obj
    





