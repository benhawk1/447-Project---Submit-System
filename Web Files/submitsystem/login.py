# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 20:33:19 2020

@author: benhawk1
"""
# This tool provides a login related functions for users. loginValidation will take in a given username and password
# and compare them to the information in the database on file in order to confirm their validity.
# Hashing will hash the given password and compare it to the password on record. If it is identical,
# true is returned. If not, false is returned. The submit function checks if a file path entered and the file type
# given are valid. If they are, then the submission will be sent to the proper folder (once it is setup properly).
import pandas as pd
import hashlib
import os


# Function that checks if the user's login information is accurate.
def loginValidation(user, passcode):
    df = pd.read_csv("submitsystem/Users.csv")
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
            if ext not in [".py", ".cpp", ".h", ".c", ".txt"]:
                print("Invalid file type specified.\n")
            else:
                valid = True
    print("File Submitted.\n")
