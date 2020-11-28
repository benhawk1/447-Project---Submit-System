import hashing
import pandas as pd

# This test works on hashing.py, using the program to add or modify a row to the csv file storing user information

# Replace these values with the desired information to be implemented into the CSV file:
row = 1  # Indices for rows start at 1
name = "Will Red"
username = "Will1"
password = "My Password"
email = "Red@umbc.edu"
role = "P"  # Can be S for student, or P for Professor

# Replace path below with the current location of the Users.csv file
loginInfo = pd.read_csv("C:/Users/benha/Documents/CMSC 447 Project/Users.csv")
loginInfo.at[row, 'Name'] = name
loginInfo.at[row, 'Role'] = role
loginInfo.at[row, 'Username'] = username
loginInfo.at[row, 'Password'] = password  # This is done so that passwords can be found by developers for use in
                                          # Testing. This column will be removed in the final iteration.
loginInfo.at[row, 'Email'] = email
hashing.encode(password, row, loginInfo)

# Open the CSV file to see your output!


