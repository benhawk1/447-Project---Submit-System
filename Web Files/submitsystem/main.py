import login
import assignments
import newStudent
import pandas as pd


# This will be the primary basis for code ran by the backend of this program, if the user were to access the submission
# system through ssh. This tool first provides a login loop for users.
# An individual will enter their username and password.
# The program will search a csv file of users for the specified username. If it is found,
# It will hash the given password and compare it to the password on record. If it is identical,
# The user is accepted into the program. If not, the user is asked to enter new information.
# Once the user is logged in, they will have the option to either exit the tool, or submit an assignment.
# If the user chooses to submit an assignment, then they will enter a path to the specified file. If the
# File is of an improper type or the path is invalid, they will be prompted to enter another path.

# Only runs if the file is ran directly, prevents this code from running in test files
if __name__ == '__main__':
    # Reads in a csv file of users, replace the string with the desired path
    loginInfo = pd.read_csv("C:/Users/benha/Documents/CMSC 447 Project/Users.csv")

    # Receives an initial set of login information from the user.
    username = input("Hello User. Please Enter Username: ")
    password = input("Please enter password: ")
    check = login.loginValidation(username, password, loginInfo)

    # Loops user input while incorrect information is provided
    while not check:
        username = input("Incorrect login information. Please enter a new username: ")
        password = input("Please enter password: ")
        check = login.loginValidation(username, password, loginInfo)
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

    if role == 'S':
        # Runs a loop that controls what student users can do. Will exit and terminate
        # the program when the user enters "Exit".
        while choice != "Exit":
            choice = input("Please enter a selection:\n\"Submit\" if you wish to submit an assignment."
                           "\n\"Exit\" if you wish to logout.\n")
            if choice == "Submit":
                login.submit()

    if role == 'P':
        # Runs a loop that controls what professors can do. Will exit and terminate
        # the program when the user enters "Exit".
        while choice != "Exit":
            choice = input("Please enter a selection:\n\"Submit\" if you wish to submit an assignment."
                           "\n\"Exit\" if you wish to logout.\n\"Add Student\" if you wish to add a student to a class."
                           "\n\"Create Assignment\" If you wish to create an assignment for one of your courses.\n")
            if choice == "Submit":
                login.submit()
            if choice == "Add Student":
                newStudent.getStudentInfo(rowNum)
            if choice == "Create Assignment":
                assignments.addAssignment(rowNum, loginInfo)
