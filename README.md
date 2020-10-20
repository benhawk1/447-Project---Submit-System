# 447-Project---Submit-System README
Iteration 1

Virtual Victory, Professor Eric Hamilton, CEO

Ben Hawkins

Jamar Reeves

Nicholas Proulx

Carly Heiner

Zachary Federci







Current Work:
The work for Iteration 1 of the Submission System has been divided according to the following sections:
Ben Hawkins - Backend Code for the Login System (All files within the “Login Files” folder)
Jamar Reeves - Frontend Code for the Submission System
Carly Heiner - Middleware for Login and Submission System.
Nicholas Proulx - Backend for student submissions into MongoDB database
Zachary Federici  - Frontend Code for Login System 

As of now, the html files for the frontend and the python code for the backend of the login system are disjoint. These aspects of the system will be connected over the next two iterations.

Installation and Operation Instructions
In order to run all code and tests for this iteration of the project, the following tools are required:

-Python 3.8
	Pip install:
-Pandas 1.1.3
-Pymongo 3.11.0
-Django 3.1.2 
-The latest version of MongoDB
	-An established instance of MongoDB
-Any web browser of choice

Login System Backend
Pulls made at https://github.com/benhawk1/447-Project---Submit-System/pull/23 and https://github.com/benhawk1/447-Project---Submit-System/pull/24

Files for this section include:
Users.csv - A csv file containing dummy login information for the purposes of testing the existing login system. Passwords in this file are presently stored in both a hashed format (for security testing) and in plaintext, so that testers can easily obtain the passwords. For proper implementation, the plaintext passwords will be removed.
hashing.py - A python program that hashes a given password, and writes the hashed result into a csv file.
login.py - A python program that obtains a username and password from the user. If these credentials match information inside of the csv file, then the user will be logged into the given system. If not, they will be prompted to enter new information. Once the user is logged in, they will have the ability to either exit the system, or submit a project. If they choose to submit a project, they will be asked to input a file path. This file path will be checked for validity, and to see if it leads to a python, C, or C++ file. If these parameters are not met, it will ask the user to enter a new path. If these parameters are met, a success message will be displayed. (No files will actually be uploaded as of now by this program in particular)
Hashing test.py and login test.py - Tests for the previously mentioned login and hashing programs that ensure functions within these files are functioning correctly.

-In order to run the code and tests for the backend of the login system (All files within the “Login Files” folder), all files should be downloaded into a designated folder. Before running any code for this section of the program, the user should update the paths listed in login.py, hashing.py, and their respective test files to the new path on your computer that leads to the downloaded Users.csv file. 
-If you wish to run login.py, all you need to do is open and run the file itself. It will prompt you to enter a correct username and password (which you can find in the Users.csv file), and then will ask you if you wish to exit or submit. If you want to submit, you can then enter a valid path to either a python, C, or C++ file.
-If you wish to run hashing test.py, there’s information for the user to fill in within the file. The user needs to enter a row to be filled in the csv file, a first and last name, a username, a password to be converted to a key, an email, and a role (S for student or P for professor). Upon filling in this information accordingly, simply run the file to perform the test. While there is no output to the terminal, the selected row should have the appropriate information stored, along with the hashed key for the entered password.
-If you wish to run login test.py, simply open the file in an appropriate IDE, and run the program. The program includes several test cases for the loginValidation and hashing functions within login.py, and the assumed outputs are commented next to each function call. If you wish to test different variables, simply edit the arguments in the calls accordingly (loginValidation takes in a username, password, and dataframe. The dataframe should not be modified. Hashing takes in a password, row, and dataframe. The dataframe should not be modified). 

Submission System Backend
Files for this section include: 
submission_backend.py
submission_backend_tests.py (for testing)
hello_world.py (for testing)
-In order to run the submission backend, you will need to install MongoDB, and then make sure the instance is running in the background. If on Windows 10, you can go into “Services” and make sure that the MongoDB service has a “Running” status. You will also need to install the appropriate python packages, such as pymongo and pytz.

Submission System and Login System Frontend
Files for this section include:
submissionPage.html - This is the primary file for this section of the iteration. This webpage features a button that allows the user to choose a file to be uploaded into the database. As development progresses, it is expected that this page will be updated as needed for ease of use. 

loginPage.html - This is where a user would log in to access the submission system. There are two boxes for a user to enter their username and password, and a login button for the user to press to log in.  

contactPage.html - This is a minimalistic page including a table with the developers names and their email addresses. On the navbar of any other page, clicking “Contact” will route here. 

Testing - For this iteration everyone in the group downloaded the corresponding webpage and opened it locally on their machine to test the functionality. Each page is responsive when adjusting window size vertically and horizontally. The footer is fixed to the bottom of the window, no matter the size of the window. 

In order to run the submission frontend, since at the moment only consists of html and css files no special software is needed to run these outside of you favorite web browser of choice. Chrome was used for testing, but the layout of the file works across Internet Explorer, Opera, Firefox, and Edge. Was unable to get a working version of Safari web browser to test the website within that browser.

Submission System and Login System Middleware

The files for this section are located in the Web Files directory.  They were developed on the feature/siteinit branch and have two completed pull requests for merging into develop: https://github.com/benhawk1/447-Project---Submit-System/pull/25 and https://github.com/benhawk1/447-Project---Submit-System/pull/27.
Relevant files in Web Files/umbcsubmitsystem/:
Settings.py - Paths for the loaders to find the static files (css and images) and templates had been edited here.  The secret key is also removed and must be added before running
Urls.py - The urls for the submitsystem app are included here.
Relevant files in Web Files/submitsystem/:
Urls.py - The urls for the login (index), contact, home, submit, and result pages are created here.  The submit and result pages are currently not in use.
Html files in templates/submitsystem - The tags and variables that the view will use are added in these files.
Forms.py - The forms used by the login and home pages are created here.  The login form requires and username and password and the home page accepts a file submission.
Views.py - The login (index), contact, home, submit, and result pages are rendered here.  The login page gets a username and password from the user.  As long as the user enters something in both input boxes, this will be treated as valid login information and the user will be redirected to the home page.  The home page allows the user to submit a file.  When the user uploads a file, it is written to the uploads directory and then saved in the database.  Clicking the home or contact links at the top of each page brings the user to these pages.
Tests.py - The unit tests for iteration one are created here.  They test that it is possible to visit each page (login (index), contact, home, submit, and result) and that the login and home pages accept user entry correctly.

To run:
Ensure that Python 3.8 is installed with pymongo and django.  Have MongoDB installed and mongo.exe running
In Web Files/umbcsubmitsystem/settings.py.  Edit line 23: SECRET_KEY = '' to include the key provided in keys.txt in the currently empty string.
In Web Files, run: python manage.py runserver
In a browser, go to http://127.0.0.1:8000/submitsystem/
You will be brought to the login page.  Enter any text in the username and password fields and click Log In.
You will be redirected to the home page.  Click contact in the top left banner to visit the contact page, click home to go back to the home page.
On the home page, click Choose File, select a file, and click Submit to submit a file.  The page will reload and the file entry will be empty again.

To test:
Complete steps 1 and 2 in “to run” if you have not already done so.
In Web Files, run: python manage.py test submitsystem
Sample expected output:
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.046s

OK
Destroying test database for alias 'default'...
