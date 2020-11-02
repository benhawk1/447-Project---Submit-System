import newStudent
import pandas as pd

# The function attempts to add the following classes and sections to the specified account. If they are
# already added to the user, then nothing new will be added. The first number is the class number, the second number
# is the section number. Feel free to change both of these numbers as desired. As well, you can check the csv file
# directly to see these changes
newStudent.addStudent("441", "4", "John1@umbc.edu")
newStudent.addStudent("421", "1", "John1@umbc.edu")
newStudent.addStudent("447", "3", "John1@umbc.edu")
newStudent.addStudent("341", "1", "John1@umbc.edu")

# Loads in the given csv file
loginInfo = pd.read_csv("C:/Users/benha/Documents/CMSC 447 Project/Users.csv")


# Obtains the information for the specified user
rowNumber = int(loginInfo[loginInfo['Email'] == "John1@umbc.edu"].index[0])
classes = loginInfo.at[rowNumber, 'Classes']
sections = loginInfo.at[rowNumber, 'Sections']

# Prints out the current classes and sections the users are listed for
print(classes)
print(sections)
