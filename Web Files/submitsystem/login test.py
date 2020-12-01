
import pandas as pd
import login
# This file includes basic tests for the hashing and loginValidation functions within login.py.
# Feel free to edit the strings and rows within these tests if you wish to check different values.
# (This may change the results of the tests)

# Replace path below with the current location of the Users.csv file
loginInfo = pd.read_csv("C:/Users/benha/Documents/CMSC 447 Project/Users.csv")

# Checks to see if the given username and password are in the specified database
print(login.loginValidation("John1", "Hello", loginInfo))        # Prints False
print(login.loginValidation("", "", loginInfo))                  # Prints False
print(login.loginValidation("John1", "Eggs", loginInfo))         # Prints True (If csv was not edited)
print(login.loginValidation("Will1", "My Password", loginInfo))  # Prints True (If csv was not edited)

# Checks to see if a given password is at a specified row in the database
print(login.hashing("My Password", 0, loginInfo))  # Prints False
print(login.hashing("My Password", 1, loginInfo))  # Prints True


