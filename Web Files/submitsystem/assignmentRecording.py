import pandas as pd

assignmentInfo = pd.read_csv("submitsystem/Assignments.csv")
loginInfo = pd.read_csv("submitsystem/Users.csv")


# Records the information for a given assignment when it is first created.
# Should be called upon creation of any assignment.
def recordAssignment(classes, sections, name, dueDate, dueTime):
    assignmentInfo.loc[len(assignmentInfo.index)] = [name, classes, sections, dueDate, dueTime]
    assignmentInfo.to_csv("submitsystem/Assignments.csv", index=False)

# Finds all assignment names for a given class and section.
# To be called when a student needs to submit an assignment and needs to select a class.
def getAssignments(myClass, mySection):
    # Creates an empty list to store assignment names
    myAssignments = []
    # Iterates through the dataframe, finding any valid assignments and adds them to the list
    for i in range(0, len(assignmentInfo.index)):
        if int(assignmentInfo.at[i, "Class"]) == myClass:
            if assignmentInfo.at[i, "Sections"] == 'All' or int(assignmentInfo.at[i, "Sections"]) == mySection:
                myAssignments.append(assignmentInfo.at[i, "Name"])
    # Returns a filled list
    return myAssignments

# Finds the classes and sections for a given user, and returns a list with odd indices being classes, and the following
# index being the corresponding section.
def getClasses(username):
    # Creates an empty list to store course information
    classInformation = []
    # Finds the row number of the user
    rowNumber = int(loginInfo[loginInfo['Username'] == username].index[0])
    # Obtains the courses and sections for the user
    myClasses = str(loginInfo.at[rowNumber, 'Classes'])
    mySections = str(loginInfo.at[rowNumber, 'Sections'])
    myClassesList = list(myClasses.split(","))
    mySectionsList = list(mySections.split(","))
    # Adds the courses and sections to a list
    for i in range(0, len(myClassesList)):
        classInformation.append(myClassesList[i])
        classInformation.append(mySectionsList[i])

    # Returns the class list
    return classInformation

#Removes a specified assignment from the registry
def removeAssignment(name, myClass, mySection):
    indexRemoval = []

    #Gets a list of assignments to remove
    assignmentInfoTemp = assignmentInfo
    for i in range(0, len(assignmentInfo.index)):
        if int(assignmentInfo.at[i, "Class"]) == myClass:
            if int(assignmentInfo.at[i, "Sections"]) == mySection:
                if assignmentInfo.at[i, "Name"] == name:
                    indexRemoval.append(i)

    #Removes all designated assignments, saves the results
    assignmentInfoTemp = assignmentInfoTemp[~assignmentInfo.index.isin(indexRemoval)]
    assignmentInfoTemp.to_csv("submitsystem/Assignments.csv", index=False)






