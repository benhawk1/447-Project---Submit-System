# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 20:33:19 2020

@author: benhawk1
"""
# This tool provides a login loop for users. An individual will enter their username and password.
# The program will search a csv file of users for the specified username. If it is found,
# It will hash the given password and compare it to the password on record. If it is identical,
# The user is accepted into the program. If not, the user is asked to enter new information.
# Once the user is logged in, they will have the option to either exit the tool, or submit an assignment.
# If the user chooses to submit an assignment, then they will enter a path to the specified file. If the
# File is of an improper type or the path is invalid, they will be prompted to enter another path.
import pandas as pd
import hashlib
import os


# Function that checks if the user's login information is accurate.
def loginValidation(user, passcode, df):
    valid = False
    userExists = df['Username'].isin([user]).any()
    if userExists:
        rowNumber = int(df[df['Username'] == user].index[0])
        valid = hashing(passcode, rowNumber, df)
    return valid


# All passwords use the same salt, may want to change
# Hashes the specified password and checks if the hashed result is on file
def hashing(passcode, row, df):
    salt = b'1\xcc\xf09V\x1b\xed\xf5\x87\x13p\xe7/3ZA\x80\xdfN\t\xd1P\xa1\xf9\x95\xc7T\xfe\x19\xa0\xd4\x0b'
    key = hashlib.pbkdf2_hmac('sha256', passcode.encode('utf-8'), salt, 100000, dklen=128)
    if str(key) == df.at[row, 'Key']:
        return True
    else:
        return False


# Receives a specified path as an input.
# If the path is invalid, asks the user to send another path.
def submit():
    valid = False
    while not valid:
        path = input("Please enter a path to your submission: ")
        exist = os.path.exists(path)
        name, ext = os.path.splitext(path)
        if not exist:
            print("Incorrect path specified.\n")
        else:
            if ext not in [".py", ".cpp", ".h", ".c"]:
                print("Invalid file type specified.\n")
            else:
                valid = True
    print("File Submitted.\n")


# Only runs if the file is ran directly, prevents this code from running in test files
if __name__ == '__main__':
    # Reads in a csv file of users, replace the string with the desired path
    loginInfo = pd.read_csv("C:/Users/benha/Documents/CMSC 447 Project/Users.csv")

    # Receives an initial set of login information from the user.
    username = input("Hello User. Please Enter Username: ")
    password = input("Please enter password: ")
    check = loginValidation(username, password, loginInfo)

    # Loops user input while incorrect information is provided
    while not check:
        username = input("Incorrect login information. Please enter a new username: ")
        password = input("Please enter password: ")
        check = loginValidation(username, password, loginInfo)
    print("Welcome " + username + "!")

    # Sets variables for the user once they are logged in
    password = 0
    rowNum = int(loginInfo[loginInfo['Username'] == username].index[0])
    role = loginInfo.at[rowNum, 'Role']

    # If the user is listed as a student in the csv file, prints out a statement confirming such.
    if role == 'S':
        print('You are a student.')

    # Establishes a string for input.
    choice = ""

    # Runs a loop that controls what the user can do. Will exit and terminate the program when the user enters "Exit".
    while choice != "Exit":
        choice = input("Please enter a selection:\n\"Submit\" if you wish to submit an assignment."
                       "\n\"Exit\" if you wish to logout.\n")
        if choice == "Submit":
            submit()
