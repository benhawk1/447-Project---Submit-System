# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 20:33:19 2020

@author: benhawk1
"""
# This tool provides functions that will either accept a csv file, or a student's email. If a csv file is
# taken as an argument, the csv file will be read into a dataframe and all the students inside will be added to the
# specified classes. If an email is taken as an argument, then the individual student connected to that email will be
# added to the specified class

import pandas as pd
import numpy as np

loginInfo = pd.read_csv("C:/Users/benha/Documents/CMSC 447 Project/Users.csv")
loginInfo = loginInfo.fillna("NA")


# A function used to add an individual student to a class by email
def addStudent(course, section, email):
    # Checks if the email currently exists in the system
    userExists = loginInfo['Email'].isin([email]).any()

    # If the user exists, attempts to add the student to the system
    if userExists:
        # Obtains the current class lists and sections of the user
        rowNumber = int(loginInfo[loginInfo['Email'] == email].index[0])
        classes = str(loginInfo.at[rowNumber, 'Classes'])
        sections = str(loginInfo.at[rowNumber, 'Sections'])
        classes = list(classes.split(","))
        sections = list(sections.split(","))
        role = loginInfo.at[rowNumber, 'Role']

        # If the user had no classes, clears the list
        if "NA" in classes:
            classes.remove("NA")
        if "NA" in sections:
            sections.remove("NA")

        # If the user had one class, convers the class and section numbers from floats to integers
        for i in range(len(classes)):
            if classes[i].endswith('.0'):
                classes[i] = classes[i].replace('.0', '')
            if sections[i].endswith('.0'):
                sections[i] = sections[i].replace('.0', '')

        # If the user is a professor, ensures that the section and class are not duplicated
        if role == 'P':
            for i in range(len(classes)):
                if classes[i] == course:
                    if sections[i] == section:
                        return -2

        # If the user is a student, ensures that they are not in the same class twice
        if role == 'S':
            for i in range(len(classes)):
                if classes[i] == course:
                    return -2

        # Adds the new class to the list, and saves it to the file
        classes.append(str(course))
        classes = ",".join(classes)
        loginInfo.at[rowNumber, 'Classes'] = classes

        # Adds the new section to the list, and saves it to the file
        sections.append(str(section))
        sections = ",".join(sections)
        loginInfo.at[rowNumber, 'Sections'] = sections

        # Saves the csv
        loginInfo.to_csv("C:/Users/benha/Documents/CMSC 447 Project/Users.csv", mode='w', index=False)

        return 1
    return -1


# Obtains student information as an input from the main function
def getStudentInfo(row):
    # Gets the email of the student to add to a class
    email = input("Please enter the student's email: ")
    userExists = loginInfo['Email'].isin([email]).any()

    # Ensures that the email is accurate
    if userExists is False:
        email = input("Invalid email. Please enter the student's email: ")

    # Obtains information for eligible classes and sections re assignment creation
    classes = str(loginInfo.at[row, 'Classes'])
    sections = str(loginInfo.at[row, 'Sections'])
    classes = list(classes.split(","))
    sections = list(sections.split(","))
    maxCount = len(classes)

    # Obtains a list of all unique classes taught by the current user
    myClasses = list(set(classes))
    myClassesCount = len(myClasses)

    # Prints possible classes, and obtains a class for assignment creation
    print("The list of potential classes to assign this student to are as follows:")
    for i in range(myClassesCount):
        print(myClasses[i])
    chosenClass = input("Please enter the correct class: ")
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
    chosenSection = input("Please enter a section number: ")
    while chosenSection not in eligibleSections:
        chosenSection = input("Invalid section choice. Please enter a valid section: ")

    addStudent(chosenClass, chosenSection, email)


#A blank function that will be used to add csv files once we obtain the proper format
def addStudents(course, section, students):
    return 0
