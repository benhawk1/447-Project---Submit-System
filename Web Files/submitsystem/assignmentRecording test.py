import assignmentRecording

#Temporarily adds a test project to the Assignments.csv file
assignmentRecording.recordAssignment(341, 1, 'testProject', '07-14-2021','23:59')

#Prints the class information for the given user below. This can be replaced with another username
print(assignmentRecording.getClasses('Doe5'))

#Prints the newly created assignment
print(assignmentRecording.getAssignments(341, 1))

#Deletes the newly created assignment from the record
assignmentRecording.removeAssignment('testProject', 341, 1)

