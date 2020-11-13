#UMBC CSEE Submit System README
##Iteration 2

Virtual Victory, Professor Eric Hamilton, CEO

Ben Hawkins

Jamar Reeves

Nicholas Proulx

Carly Heiner

Zachary Federci


###Current Work:

The work for Iteration 2 of the Submission System has been divided according to the following sections:

Ben Hawkins - Backend work for assignment creation, student class assignment, work on connecting login system

Jamar Reeves - Frontend Code for the HomePage

Carly Heiner - Middleware for home, contact, submit, student manager, and assignments page, work on connecting login system

Nicholas Proulx - Backend for section creation, student management (adding/removing students, changing student names), assignment addition/removal

Zachary Federici  - Frontend Code for AssignmentPage, Student Management Page 

As of now, the html files for the frontend and the python code for the backend of the login system are disjoint. These aspects of the system are expected to be completed over Iteration 3.

###Installation and Operation Instructions

In order to run all code and tests for this iteration of the project, the following tools are required:

-Python 3.8

-Pip install:
	
-Pandas 1.1.3

-Pymongo 3.11.0

-Django 3.1.2 

-django-crispy-forms

-The latest version of MongoDB

-An established instance of MongoDB

-Any web browser of choice

####Login System Backend
Files for this section include:

Users.csv - A csv file containing dummy login information for the purposes of testing the existing login system. Passwords in this file are presently stored in both a hashed format (for security testing) and in plaintext, so that testers can easily obtain the passwords. For proper implementation, the plaintext passwords will be removed.

hashing.py - A python program that hashes a given password, and writes the hashed result into a csv file.

Login.py - A python program that assists with the login verification process used by main.py

main.py - A python program that obtains a username and password from the user. If these credentials match information inside of the csv file, then the user will be logged into the given system. If not, they will be prompted to enter new information. Once the user is logged in, they will have the ability to either exit the system, or submit a project. If they choose to submit a project, they will be asked to input a file path. This file path will be checked for validity, and to see if it leads to a python, C, or C++ file. If these parameters are not met, it will ask the user to enter a new path. If these parameters are met, a success message will be displayed. (No files will actually be uploaded as of now by this program in particular)

Hashing test.py and login test.py - Tests for the previously mentioned login and hashing programs that ensure functions within these files are functioning correctly.

See section below for testing purposes.

####User Assignment and New Student Backend
Files for this section include:

assignments.py - A python program that looks at the current professor making an assignment, and has them enter a desired class and section (or all sections). If it is not a section or class that they are teaching, it asks them to enter a new section. It will then have the professor enter a name for the assignment, and a due date and time. If the due date and time are not in the valid format or are out of range, it will prompt for this information again. This information will then be printed back to the user (later to be stored)

newStudent.py - A python program that takes in a user’s email, and adds them to a new class and section that are also passed in. There are checks to ensure that a user is not added to the same class and section multiple times. This information is then saved back into the login csv file that is used for validation purposes.

Assignments test.py - This program prompts the user to enter one of the listed courses. If it is incorrect, it will prompt the user again. If it is correct, it will then prompt for a section to create an assignment for, and then a name, date, and time. If these fields are invalid, it will reprompt.

newStudent test.py - Tests the functionality of newStudent.py by adding classes to several existing students. If the same class and section are already listed for the student, then they will not be added a second time. It will then print all of the classes and sections the student is currently registered for.

-In order to run the code and tests for the backend of the login system and assignment/student system (All files within the “Login Files” and “Assignment and Student Files” folders), all files should be downloaded into a designated folder. Before running any code for this section of the program, the user should update the paths listed in the provided files and their respective test files to the new path on your computer that leads to the downloaded Users.csv file. 

-If you wish to run hashing test.py, there’s information for the user to fill in within the file. The user needs to enter a row to be filled in the csv file, a first and last name, a username, a password to be converted to a key, an email, and a role (S for student or P for professor). Upon filling in this information accordingly, simply run the file to perform the test. While there is no output to the terminal, the selected row should have the appropriate information stored, along with the hashed key for the entered password.

-If you wish to run login test.py, simply open the file in an appropriate IDE, and run the program. The program includes several test cases for the loginValidation and hashing functions within login.py, and the assumed outputs are commented next to each function call. If you wish to test different variables, simply edit the arguments in the calls accordingly (loginValidation takes in a username, password, and dataframe. The dataframe should not be modified. Hashing takes in a password, row, and dataframe. The dataframe should not be modified).

-If you wish to run main.py, all you need to do is open and run the file itself. It will prompt you to enter a correct username and password (which you can find in the Users.csv file), and then will ask you if you wish to exit or submit or utilize some of the professor functions based on the account you choose. If you want to submit, you can then enter a valid path to either a python, C, or C++ file.

-If you wish to run assignments test.py or newStudent test.py, simply run the given files. For newStudent test, the classes and sections in the first region of code can be edited if you wish to test adding more classes to the given student. For assignments test.py, all of the information will be entered through the terminal.

-The files login.py, hashing.py, newStudent.py, and assignments.py only consist of functions, and as a result should not be ran on their own. 


####Section and Student Management Backend
Files for this section include:
section_management.py -- In charge of adding/deleting sections, adding/removing students from those sections, and adding/removing assignments to and from each section. Sections are added by creating a new document (specifically, a dictionary) that contains the section’s information -- particularly, the section number, assignments for that section, and students in that section. The assignments for the section are represented as a list of dictionaries, as are the students. The submit system has been updated such that when a student submits their assignment, that submission (in the form of a dictionary) is appended to the list of submissions for that student. This file must be paired with db_func.py. 

db_func.py -- Contains common pymongo functions such as dropping collections, connecting to clients, etc, that are shared among the other files (section_management, submission_backend, etc).

Testing -- section_management_tests.py -- tests each function in section_management.py and prints the result of each. Uses “hw1.txt” to test creating assignments.

####Submission, Login, Contact, Home, Assignment, and Student Management Pages Frontend
Files for this section include:
submissionPage.html - This is the primary file for this section of the iteration. This webpage features a button that allows the user to choose a file to be uploaded into the database. As development progresses, it is expected that this page will be updated as needed for ease of use. 

loginPage.html - This is where a user would log in to access the submission system. There are two boxes for a user to enter their username and password, and a login button for the user to press to log in.  

contactPage.html - This is a minimalistic page including a table with the developers names and their email addresses. On the navbar of any other page, clicking “Contact” will route here. 

newHomePage.html - This is a minimalistic page including a table that will be dynamically updated with the students of a class and their corresponding information.

AssignmentPage.html - This page is for the purpose of a professor adding or removing assignments. It includes a select box with the options of either Create or Remove, a number selector for choosing what class the professor teaches (temporary, to be a select box of classes professor teaches when frontend and backend connect successfully), multiple checkbox options for sections (temporary, to be a multiple checkbox of actual sections the professor teaches for the class selected, again once frontend and backend connect successfully), textbox to enter the name of the assignment, datetime input to select what day and time the assignment is due, and multiple file uploads for rubrics and other documents. 

studentManagementPage.html - This page is for the purpose of adding and removing students from a class. It includes a select box with the options of either Add or Remove, a number selector for choosing what class the professor teaches (temporary, to be a select box of classes professor teaches when frontend and backend connect successfully), single checkbox options for sections to add/remove the student, text boxes for the students first name, last name, and UMBC email address, and a file uploader for the purpose of uploading a csv file with student information. If a csv file is uploaded, then that will be considered over information entered manually on the page.

Testing - For this iteration everyone in the group downloaded the corresponding webpage and opened it locally on their machine to test the functionality. Each page is responsive when adjusting window size vertically and horizontally. The footer is fixed to the bottom of the window, no matter the size of the window. 

In order to run the submission frontend, since at the moment only consists of html and css files no special software is needed to run these outside of you favorite web browser of choice. Chrome was used for testing, but the layout of the file works across Internet Explorer, Opera, Firefox, and Edge. Was unable to get a working version of Safari web browser to test the website within that browser.

####Home, Contact, Submit, Student Manager, and Assignments Middleware
The files for this section are located in the Web Files directory.  They were developed on the feature/assignmentpage, feature/home_and_contact_pages, and feature/studentmngmt branches and have four completed pull requests for merging into develop: https://github.com/benhawk1/447-Project---Submit-System/pull/37, https://github.com/benhawk1/447-Project---Submit-System/pull/43, https://github.com/benhawk1/447-Project---Submit-System/pull/44, and https://github.com/benhawk1/447-Project---Submit-System/pull/45.

#####Relevant files in Web Files/umbcsubmitsystem/:

Settings.py - Paths for the loaders to find the static files (css and images) and templates had been edited here.  The secret key is also removed and must be added before running

Urls.py - The urls for the submitsystem app are included here.

#####Relevant files in Web Files/submitsystem/:

Urls.py - The urls for the login (index), contact, home, submit, student manager and assignments pages are created here.

Html files in templates/submitsystem - The tags and variables that the view will use are added in these files.

Forms.py - The forms used by the login, submit, student manager, and assignments pages are created here.  The login form requires and username and password; the submit page accepts a file submission; the student manager page requires a choice between add and remove, class number, section, first name, last name, and student ID, it does not yet support the csv upload option; and the assignment page requires a choice between create and remove, class number, section, assignment name, date and time due, and instruction file upload.

Views.py - The login (index), contact, home, submit, student manager, and assignments pages pages are rendered here.  The login page gets a username and password from the user.  As long as the user enters something in both input boxes, this will be treated as valid login information and the user will be redirected to the home page.  The home page shows a sample professor’s view of their class roster.  At the top of every page but the login page, the user can click the home, contact, submit, student manager, and assignments links to be taken to the corresponding.  When the user uploads a file on the submit page, it is written to the uploads directory and then saved in the database.  A message is displayed at the bottom to confirm the submission. On the student manager page, a professor can add or remove students by entering the requested information.  An AttributeError currently prevents the actual addition or removal of the student in the database.  On the assignments page, a professor can create or remove and assignment by entering the requested information and uploading an instructions file.  The same error in the database occurs.

Tests.py - The unit tests for iteration one and two are created here.  They test that it is possible to visit each page (login (index), contact, home, submit, student manager, and assignments) and that the login, submit, student manager, and assignment pages accept user entry.

#####To run:
1. Ensure that Python 3.8 is installed with pymongo and django.  Have MongoDB installed and mongo.exe running
2. In Web Files/umbcsubmitsystem/settings.py.  Edit line 23: SECRET_KEY = '' to include the key provided in keys.txt in the currently empty string.
3. In Web Files, run: python manage.py runserver
4. In a browser, go to http://127.0.0.1:8000/submitsystem/
5. You will be brought to the login page.  Enter any text in the username and password fields and click Log In.
6. You will be redirected to the home page.  Click any link in the top left banner to visit the corresponding page.
7. On the submit page, click Choose File, select a file, and click Submit to submit a file.  A “File submitted” message will appear when the file is accepted.
8. On the student manager page, choose to add or remove a student, enter a class number, select a section, and enter a first name, last name, and student ID.  The student roster csv is not yet supported. Click submit.  If your input is valid, an AttributeError will occur.
9. On the assignments page, choose to create or remove an assignment, enter a class number, select a section, and enter an assignment name and due date (MM/DD/YYYY).  Click Choose File and upload an instructions file.  Click submit.  If your input is valid, an AttributeError will occur.

#####To test:
1. Complete steps 1 and 2 in “to run” if you have not already done so.
2. In Web Files, run: python manage.py test submitsystem
3. Sample expected output:

Creating test database for alias 'default'...

System check identified no issues (0 silenced).

.....

Ran 9 tests in 0.066s

OK

Destroying test database for alias 'default'...
