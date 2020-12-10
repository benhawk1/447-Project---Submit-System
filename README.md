UMBC CSEE Submit System README
Iteration 5

Virtual Victory, Professor Eric Hamilton, CEO
Ben Hawkins
Jamar Reeves
Nicholas Proulx
Carly Heiner
Zachary Federci



Current Work:
The work for Iteration 5 of the Submission System has been divided according to the following sections:
Ben Hawkins - Worked on setting up assignment recording to operate with assignment creation, assisted with debugging and pull requests
Jamar Reeves - Assisted with testing and debugging and approved a few pull requests.
Carly Heiner -  Assisted with video planning, debugging, and testing.
Nicholas Proulx - Fine-tuning current code: had test files have more similar structure and be slightly more thorough, improved list_collection so that it lists info in separate lines, implemented get_assignments which returns a list of assignment dictionaries for a particular course/section
Zachary Federici  - Implemented scrollbar across all pages, commented out code helpful for further backend and frontend communication, prepared pages for video demo, created video demo

Notes for Those Continuing Project
Although the team did not manage to fully implement the connection between the backend and frontend, there is some code that was written and commented out that the team feels could be helpful, so that anyone continuing the project wouldn’t have to start from scratch implementing this. It exists in the following locations and is a commented out block of code in each place:
Function submissionViewer() in views.py
Function studentAssignments() in views.py
Function getfileViewer() in views.py
Function getfileAssignments() in views.py
studentAssignmentPage.html
submissionViewer.html

Installation and Operation Instructions
In order to run all code and tests for this iteration of the project, the following tools are required:

-Python 3.8
	Pip install:
-Pandas 1.1.3
-Pymongo 3.11.0
-Django 3.1.2 
-Django-crispy-forms 1.9.2
-Numpy 1.19.3 (This specific version may be needed to avoid an error on Windows)
-The latest version of MongoDB
	-An established instance of MongoDB
-Any web browser of choice

Login System Backend
ALL FILES ARE IN Web Files\submitsystem
Files for this section include:
Users.csv - A csv file containing dummy login information for the purposes of testing the existing login system. Passwords in this file are presently stored in both a hashed format (for security testing) and in plaintext, so that testers can easily obtain the passwords. For proper implementation, the plaintext passwords will be removed.
hashing.py - A python program that hashes a given password, and writes the hashed result into a csv file.
Login.py - A python program that assists with the login verification process used by main.py
main.py - A python program that obtains a username and password from the user. If these credentials match information inside of the csv file, then the user will be logged into the given system. If not, they will be prompted to enter new information. Once the user is logged in, they will have the ability to either exit the system, or submit a project. If they choose to submit a project, they will be asked to input a file path. This file path will be checked for validity, and to see if it leads to a python, C, or C++ file. If these parameters are not met, it will ask the user to enter a new path. If these parameters are met, a success message will be displayed. (No files will actually be uploaded as of now by this program in particular)
Hashing test.py and login test.py - Tests for the previously mentioned login and hashing programs that ensure functions within these files are functioning correctly.

See section below for testing purposes.

User Assignment and New Student Backend
ALL FILES ARE IN Web Files\submitsystem
Files for this section include:
assignments.py - A python program that looks at the current professor making an assignment, and has them enter a desired class and section (or all sections). If it is not a section or class that they are teaching, it asks them to enter a new section. It will then have the professor enter a name for the assignment, and a due date and time. If the due date and time are not in the valid format or are out of range, it will prompt for this information again. This information will then be printed back to the user, (later to be stored). 
assignmentRecording.py - A python program with several functions built in. recordAssignment obtains information for an assignment (class, section, name, and due date) and records it within a new csv file. getAssignments obtains the names of all assignments for a specified class and section. getClasses obtains all classes and sections that a specific user is registered for. removeAssignment removes a specified assignment from the assignment info csv.
Assignments.csv - A csv file that stores information on assignments including their Name, the class it is for, the section it is for (or All), the due date, and the due time.

newStudent.py - A python program that takes in a user’s email, and adds them to a new class and section that are also passed in. There are checks to ensure that a user is not added to the same class and section multiple times. This information is then saved back into the login csv file that is used for validation purposes. Users also have the option to upload csv files with student information in order to upload multiple students at once into the database. As well, if a student does not already exist in the database, they will be added with a random 8-digit password.
newStudent test.py - A python program that attempts to add a student into a new class. If the class has the same number and section number as a class they were already a part of, the process will fail. The test then prints the current classes and sections the student is registered for, and attempts to use a student csv to upload multiple students into Users.csv
Assignments test.py - This program prompts the user to enter one of the listed courses. If it is incorrect, it will prompt the user again. If it is correct, it will then prompt for a section to create an assignment for, and then a name, date, and time. If these fields are invalid, it will reprompt.
newStudent test.py - Tests the functionality of newStudent.py by adding classes to several existing students. If the same class and section are already listed for the student, then they will not be added a second time. It will then print all of the classes and sections the student is currently registered for.
assignmentRecording test.py - This program creates a test project for a given class and assignment. It then prints the listed classes and assignments for a specified user. After, the information for the newly created assignment is printed. This assignment is then deleted from the csv.

-In order to run the code and tests for the backend of the login system and assignment/student system, all files should be downloaded into a designated folder. Before running any code for this section of the program, the user should update the paths listed in the above files and their respective test files to the new path on your computer that leads to the downloaded Users.csv file, the Assignments.csv file, and the Students.csv file respectively. 
-If you wish to run hashing test.py, there’s information for the user to fill in within the file. The user needs to enter a row to be filled in the csv file, a first and last name, a username, a password to be converted to a key, an email, and a role (S for student or P for professor). Upon filling in this information accordingly, simply run the file to perform the test. While there is no output to the terminal, the selected row should have the appropriate information stored, along with the hashed key for the entered password.
-If you wish to run login test.py, simply open the file in an appropriate IDE, and run the program. The program includes several test cases for the loginValidation and hashing functions within login.py, and the assumed outputs are commented next to each function call. If you wish to test different variables, simply edit the arguments in the calls accordingly (loginValidation takes in a username, password, and dataframe. The dataframe should not be modified. Hashing takes in a password, row, and dataframe. The dataframe should not be modified).
- If you wish to run main.py, all you need to do is open and run the file itself. It will prompt you to enter a correct username and password (which you can find in the Users.csv file), and then will ask you if you wish to exit or submit or utilize some of the professor functions based on the account you choose. If you want to submit, you can then enter a valid path to either a python, C, or C++ file.
-If you wish to run assignments test.py or newStudent test.py, simply run the given files. For newStudent test, the classes and sections in the first region of code can be edited if you wish to test adding more classes to the given student. For assignments test.py, all of the information will be entered through the terminal.

-The files login.py, hashing.py, newStudent.py, and assignments.py only consist of functions, and as a result should not be ran on their own. 


Connecting Backend to Frontend/Middleware
For this iteration, a new file called authentication.py was created that handles connecting the website to the login system in login.py. If the information is valid, the user is logged in, and if not, they will need to enter new credentials.
Tests, list_collection, get_assignments
Files for this section include:
submission_backend_tests.py - Renamed and moved some variables around to more closely match the format in section_management_tests.py. Also included extra tests to specifically test late submissions versus on-time submissions. 
db_func.py - list_collection now gives a more readable output by listing information such as student dictionaries, assignments, etc on separate lines, rather than simply printing the entire course dictionary on a single line. The downside is that this function now assumes the specific format of the course dictionary, so if a differently-formatted collection is passed into the function, it will crash.
submit_file.py - get_assignments has been added. This function searches for a specific course/section and returns the list of assignment dictionaries.

Submission, Login, Contact, Home, Assignment, and Student Management Pages Frontend
Files for this section include:

submissionPage.html - This page allows the professor to select a class they teach, a section they teach, an assignment, and a file to upload for submission of their own assignments.

loginPage.html - This is where a user would log in to access the submission system. There are two text boxes for a user to enter their username and password, and a login button for the user to press to log in.  

contactPage.html - This is a minimalistic page for the professor view including a table with the developers names and their email addresses.

newHomePage.html - This is a minimalistic page for when the professor logs in. It includes a table that will show the classes and sections that a professor teaches.

AssignmentPage.html - This page is for the purpose of a professor adding or removing assignments. It includes a select box with the options of either Create or Remove, a text box for choosing what class the professor teaches, multiple checkbox options for sections the professor teaches, textbox to enter the name of the assignment, datetime input to select what day and time the assignment is due, and multiple file uploads for rubrics and other documents.

studentManagementPage.html - This page is for the purpose of adding and removing students from a class. It includes a select box with the options of either Add or Remove, a text box for choosing what class the professor teaches, single checkbox options for sections to add/remove the student, text boxes for the students first name, last name, and UMBC ID, and a file uploader for the purpose of uploading a csv file with student information, if multiple students need to be added/removed, for example at the beginning or end of a semester. If a csv file is uploaded, then that will be considered over information entered manually on the page.

studentHomePage.html - this page will be for when students log in. It will display as the home page a student sees after they log in to the system. This page will display the class names and section of that class that a student is enrolled in. This page has not been connected to the system yet due to the nature of the shorter iteration and will be connected in the next iteration if time permits.

studentContactPage.html - This page will also be displayed to students. When a student is logged in and clicks on the contact navbar link they will be navigated to this page. The difference between this page and the contact page for professors is that the student's version has less navigation options available to them. This page has not been connected to the system yet due to the nature of the shorter iteration and will be connected in the next iteration if time permits.

studentSubmissionPage.html - This page is for students to submit their work. They can select their class, section, and assignment to turn in from a select box, as well as upload what they want to turn in.

studentAssignmentPage.html - This page will provide a table of all the assignments for a student, in a table showing class, section, assignment name, attachment included, due date, and due time 

submissionViewer.html - This page is for the professor to view the assignments that students turned in. They are provided with a student’s first name, last name, class, assignment name, attachment student uploaded, the submission date and time of the student, and due date and due time of the assignment.

Testing - For this iteration everyone in the group downloaded the corresponding webpage and opened it locally on their machine to test the functionality. Each page is responsive when adjusting window size vertically and horizontally. The footer is fixed to the bottom of the window, no matter the size of the window. 

In order to run the submission frontend, since at the moment only consists of html and css files no special software is needed to run these outside of you favorite web browser of choice. Chrome was used for testing, but the layout of the file works across Internet Explorer, Opera, Firefox, and Edge. Was unable to get a working version of Safari web browser to test the website within that browser.

Home, Contact, Submit, Student Manager, and Assignments Middleware
The files for this section are located in the Web Files directory.  They were developed on the feature/loginReq branch and have the following pull request for merging into develop: https://github.com/benhawk1/447-Project---Submit-System/pull/58.

Relevant files in Web Files/umbcsubmitsystem/:
Settings.py - The authentication backend, login, login redirect urls are assigned here.  Paths for the loaders to find the static files (css and images) and templates have also been edited here.  The secret key is removed and must be added before running.  
Urls.py - The urls for the submitsystem app are included here.
Relevant files in Web Files/submitsystem/:
Urls.py - The urls for the login (index), contact, home, submit, student manager, submission viewer and assignments pages are created here.
Html files in templates/submitsystem - The tags and variables that the view will use are added in these files.
Forms.py - The forms used by the login, submit, student manager , and assignments pages are created here.  The login form requires and username and password; the submit page accepts a file submission and provides dropdown selections for student class, section, and assignment name; the student manager page requires a choice between add and remove, class number, section (a widget was added to allow for one and only one section to be selected when adding a student to a class) , first name, last name, and student ID, it does not yet support the csv upload option; and the assignment page requires a choice between create and remove, class number, section (a widget was added to allow for multiple sections to be selected when adding a new assignment), assignment name, date and time due, and instruction file upload.
Authentication.py - takes in a username and password sent from the login page, and passes the information to login.py. If the login information is valid, it will check to see if a user variable has already been created under this name, and if not, it will create a new user variable with the appropriate info. This user will then be returned. If the info is invalid, the function will return none. The system will only log the user in if a user has been passed, otherwise they will need to enter new credentials. If you wish to test this functionality, please log into the system with a username and password provided within Users.csv
Views.py - The login (index), contact, home, submit, student manager, submission viewer, and assignments pages pages are rendered here.  The login page gets a username and password from the user, validated from the list of users in Users.csv.  Depending on if a student or professor account is logged in, different pages are available in the top banner links.  In the student version, the homepage displays a welcome, the contact and submit pages are the same as the professor version except that the links in the banner are different.  The assignments page shows the student a list of their assignments.  The rest of the views described are according to the professor version.  The home page shows a sample professor’s view of their class roster.  At the top of every page but the login page, the user can click the home, contact, submit, student manager, and assignments links to be taken to the corresponding page.  When the user uploads a file on the submit page, it is written to the uploads directory and then saved in the database.  A message is displayed at the bottom to confirm the submission. On the student manager page, a professor can add or remove students by entering the requested information.  The submission viewer page shows the professor information on the submissions made by their students.  On the assignments page, a professor can create or remove an assignment by entering the requested information and uploading an instructions file.
Tests.py - The unit tests for iteration one, two, three, four, and five are created here.  They test that after logging in, it is possible to visit each page (login (index), contact, home, submit, student manager, submission viewer, and assignments) and that the login, submit, student manager, and assignment pages accept user entry.

To run:
Ensure that Python 3.8 is installed.  Pip install: django, pymongo, pandas, and django-crispy-forms.  To avoid an error on Windows: make sure the version of numpy that is used is 1.19.3 by running: pip install numpy==1.19.3.  Have MongoDB installed and mongo.exe running
In Web Files/umbcsubmitsystem/settings.py.  Edit line 23: SECRET_KEY = '' to include the key provided in keys.txt in the currently empty string.
In Web Files, run: python manage.py migrate
In Web Files, run: python manage.py runserver
In a browser, go to http://127.0.0.1:8000/submitsystem/ (Please use an “incognito” window to ensure login sessions do not conflict)
You will be brought to the login page.  Enter John1 in the username field and Eggs in the password fields and click Log In.  This is a student account so you will see the student versions of the home, contact, submission, and assignments pages.  To access the professor’s pages instead, enter the username: Will1 and password: My Password.
You will be redirected to the student home page.  Click any link in the top left banner to visit the corresponding page.
On the submit page, click Choose File, select a file, and click Submit to submit a file.  Select a class, section, and assignment from the dropdown menus.  A “File submitted” message will appear when the file is accepted.
The student manager page is only directly accessible to professors.  On the student manager page, choose to add or remove a student, enter a class number, select a section, and enter a first name, last name, and student ID.  The student roster csv is not yet supported. Click submit.  If your input is valid, a “Student Successfully Added” or “Student Successfully Removed” message will appear.
The submission viewer page is only directly accessible to professors.  Click the Student Submissions links that appears on the top banner for professor accounts and you will see a sample list of student submissions.
On the student version of the assignment page, you will see a sample list of a student’s assignments.  On the professor version of the assignments page, choose to create or remove an assignment, enter a class number, select a section or sections, and enter an assignment name and due date by clicking the calendar icon.  Click Choose File and upload an instructions file.  Click submit.  If your input is valid an “Assignment Successfully Created” or “Assignment Successfully Removed” message will appear.  (The message might not be visible depending on the size of the screen and web page).

To test:
Complete steps 1, 2, and 3 in “to run” if you have not already done so.
In Web Files, run: python manage.py test submitsystem
Sample expected output:
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 16 tests in 0.240s
OK
Destroying test database for alias 'default'...
