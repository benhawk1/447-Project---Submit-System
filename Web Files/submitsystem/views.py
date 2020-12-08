from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import LoginForm, SubmitForm, StudentForm, AssignmentForm, StudentSubmitForm
from submitsystem.submission_backend import *
from submitsystem.db_func import *
from submitsystem.section_management import *
from submitsystem.authentication import *
from django.views.generic.base import TemplateView
import mimetypes
import pandas as pd


#def download_file(request):
#    f1_path = '/file/path'
#    filename = 'downloaded_file_name.extension'

#    f1 = open(f1_path,'r')
#    mime_type, _ = mimetypes.guess_type(f1_path)
#    response = HttpResponse(f1, content_type=mime_type)
#    response['Content-Disposition'] = "attachment; filename=%s" % filename
#        return response

# write submitted file to uploads folder
def handle_uploaded_file(f):
    path = 'submitsystem/uploads/' + f.name
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return path

# login page
def index(request):
    # message to display if login is invalid
    invalidLogin = ''

    # if this is a POST request, process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = LoginForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # process the input
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # log user in
                login(request, user)

                # determine if user is student or professor
                df = pd.read_csv("submitsystem/Users.csv")
                rowNumber = int(df[df['Username'] == username].index[0])
                role = df.at[rowNumber, 'Role']

                # redirect to homepage for student
                if role == "S":
                    return HttpResponseRedirect('studenthome/')

                # redirect to professor homepage
                else:
                    return HttpResponseRedirect('home/')
            else:
                invalidLogin = "Invalid login"

    # if a GET (or any other method) create a blank form
    else:
        form = LoginForm()

    return render(request, 'submitsystem/loginPage.html', {'form': form, 'invalidLogin' : invalidLogin})

# contact page
@login_required
def contact(request):
    return render(request, 'submitsystem/contactPage.html')

# submit page
@login_required
def submit(request):
    # displays message if file submitted
    fileSubmitted = ""

    # if this is a POST request, process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubmitForm(request.POST, request.FILES)

        # check whether it's valid:
        if form.is_valid():
            # process the file
            path = handle_uploaded_file(request.FILES['submission'])

            # get class, section and assignment the submission is for
            studentClass = form.cleaned_data['studentClass']
            section = form.cleaned_data['section']
            assignment = form.cleaned_data['assignment']

            # get user's ID and name (using sample ID for now)
            username = request.user.username
            df = pd.read_csv("submitsystem/Users.csv")
            rowNumber = int(df[df['Username'] == username].index[0])
            name = df.at[rowNumber, 'Name']

            # add course, section, and student (expected to say collection create failed if course already exits)
            create_collection(studentClass)
            add_section(section, studentClass)
            add_student("EH999", name, section, studentClass)

            # add to db
            submit_file("EH999", assignment, section, path, studentClass)

            # add message to display to user
            fileSubmitted = "File submitted"

    # if a GET (or any other method) create a blank form
    else:
        form = SubmitForm()

    return render(request, 'submitsystem/submissionPage.html', {'form': form, 'fileSubmitted' : fileSubmitted})

# student manager page
@login_required
def studentmanager(request):

    studentAction = ""
    # if this is a POST request, process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentForm(request.POST) #request.FILES

        # check whether it's valid:
        if form.is_valid():
            # process the input
            addRemove = form.cleaned_data['addRemove']
            classNum = form.cleaned_data['classNum']
            section = form.cleaned_data['section']
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            #email = form.cleaned_data['email'] email replaced with id to match backend
            id = form.cleaned_data['id']

            # create class and section (expected to say collection create failed if class already exits)
            create_collection(classNum)
            add_section(section, classNum)

            # add the student or remove them if add is not selected
            if addRemove == "Add":
                add_student(id, f'{firstName} {lastName}', section, classNum)
                studentAction = "Student Successfully Added"
            else:
                remove_student(id, section, classNum)
                studentAction = "Student Successfully Removed"


    # if a GET (or any other method) create a blank form
    else:
        form = StudentForm()

    return render(request, 'submitsystem/studentManagementPage.html', {'form': form, 'studentAction' : studentAction})

# assignments page
@login_required
def assignments(request):

    assignmentAction = ""

    # if this is a POST request, process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AssignmentForm(request.POST, request.FILES)

        # check whether it's valid:
        if form.is_valid():
            # process the file
            path = handle_uploaded_file(request.FILES['uploadFile'])

            # process the input
            createRemove = form.cleaned_data['createRemove']
            classNum = form.cleaned_data['classNum']
            section = form.cleaned_data['section']
            assignmentName = form.cleaned_data['assignmentName']
            datetimeDue = form.cleaned_data['datetimeDue']

            """
            if createRemove == "Create":
                actual_file_name = path.split('/')[2]
                myclient = pymongo.MongoClient("mongodb://localhost:27017")
                mydb = myclient["student_submissions"]
                mycol = mydb["assignments"]
                mydict = {"name": assignmentName, "class": classNum, "section": section, "due": datetimeDue}
                x = mycol.insert_one(mydict)
            """

            # add course and section(s) # (expected to say collection create failed if course already exits)
            create_collection(classNum)
            add_section(section, classNum)
            # create assignment or remove assignment if create is not selected
            if createRemove == "Create":
                add_assignment(section, assignmentName, path, datetimeDue, classNum)
                assignmentAction = "Assignment Successfully Created"
            else:
                remove_assignment(section, assignmentName, path, classNum)
                assignmentAction = "Assignment Successfully Removed"

    # if a GET (or any other method) create a blank form
    else:
        form = AssignmentForm()

    return render(request, 'submitsystem/AssignmentPage.html', {'form' : form, 'assignmentAction' : assignmentAction})

# student home page
@login_required
def studentHome(request):
    return render(request, 'submitsystem/studentHomePage.html')

# student contact page
@login_required
def studentContact(request):
    return render(request, 'submitsystem/studentContactPage.html')

# student submit page
@login_required
def studentSubmit(request):
    # displays message if file submitted
    fileSubmitted = ""

    # if this is a POST request, process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentSubmitForm(request.POST, request.FILES)

        # check whether it's valid:
        if form.is_valid():
            # process the file
            path = handle_uploaded_file(request.FILES['submission'])

            # get class, section and assignment the submission is for
            studentClass = form.cleaned_data['studentClass']
            section = form.cleaned_data['section']
            assignment = form.cleaned_data['assignment']

            # get user's ID and name (using sample ID for now)
            username = request.user.username
            df = pd.read_csv("submitsystem/Users.csv")
            rowNumber = int(df[df['Username'] == username].index[0])
            name = df.at[rowNumber, 'Name']


            # add course, section, and student (expected to say collection create failed if course already exits)
            create_collection(studentClass)
            add_section(section, studentClass)
            add_student("EH999", name, section, studentClass)

            # add to db (sample assignments may not exist, expected "Assignment does not exist" message)
            submit_file("EH999", assignment, section, path, studentClass)

            # add message to display to user
            fileSubmitted = "File submitted"

    # if a GET (or any other method) create a blank form
    else:
        form = StudentSubmitForm()

    return render(request, 'submitsystem/studentSubmissionPage.html', {'form': form, 'fileSubmitted' : fileSubmitted})

# student assignments page
@login_required
def studentAssignments(request):
    """
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["student_submissions"]
        mycol = mydb["assignments"]
        output = []
        for x in mycol.find({}, {"_id": 0, "due": 0}):
            output.append(x)

        context = {'data': output}
        return render(request, 'submitSystem/studentAssignmentPage.html', context)
        """
    assignment1 = ["CMSC 447", "1", "Homework 1", "hw1.pdf", "12/10/2020", "11:59"]
    assignment2 = ["CMPE 315", "3", "Lab 4", "lab4.pdf", "12/30/2020", "11:59"]
    assignments = [assignment1, assignment2]
    return render(request, 'submitsystem/studentAssignmentPage.html', {'assignments' : assignments})

# Home Page table:
@method_decorator(login_required, name='dispatch')
class homeTable(TemplateView):
    template_name = 'submitsystem/newHomePage.html'

    def get_context_data(self, **kwargs):
        context = super(homeTable, self).get_context_data(**kwargs)
        context["rosterhead"] = ['Class', 'Class Section']
        context["rosterbody"] = [{'classname':"CMSC 447", 'section':1},
                                 {'classname':"CMSC 341", 'section':2}
                                 ]
        return context

@method_decorator(login_required, name='dispatch')
class studentHomeTable(TemplateView):
    template_name = 'submitsystem/studentHomePage.html'

    def get_context_data(self, **kwargs):
        context = super(studentHomeTable, self).get_context_data(**kwargs)
        context["rosterhead"] = ['Class', 'Class Section', 'Professor First Name', 'Professor Last Name', 'E-Mail']
        context["rosterbody"] = [{'classname':"CMSC 447", 'section':1, 'firstname':'Will', 'lastname':'Greene', 'email':'Greene@umbc.edu'},
                                 {'classname':"CMPE 315", 'section':3, 'firstname':'Barry', 'lastname':'Smith', 'email':'Barry0@umbc.edu'}
                                 ]
        return context

@login_required
def submissionViewer(request):
    """
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["student_submissions"]
    mycol = mydb["assignments"]
    output = []
    for x in mycol.find({}, {"_id": 0, "due": 0}):
        output.append(x)

    context = {'data': output}
    return render(request, 'submitSystem/submissionViewer.html', context)
    """
    assignment1 = ["John", "Greene", "CMSC 447", "Homework 1", "hw1.py", "12/10/2020", "11:50", "12/10/2020", "11:59"]
    assignment2 = ["Mason", "Black", "CMSC 341", "Project 2", "proj2.cpp", "12/15/2020", "4:32", "12/14/2020", "11:59"]
    assignments = [assignment1, assignment2]
    return render(request, 'submitsystem/submissionViewer.html', {'assignments' : assignments})

"""
def getfileViewer(request):
    val = request.POST['list']
    val = val.replace("'",'"')
    y = json.loads(val)

    fname = y['first_name']
    lname = y['last_name']
    clss = y['class']
    assi = y['assignment']
    path = y['path']
    sd = y['sub_date']
    st = y['sub_time']
    dd = y['due_date']
    dt = y['due_time']

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["student_submissions"]
    mycol = mydb["assignments"]
    x = mycol.find_one({"first_name": fname, "last_name": lname, "class": clss, "assignment": assi, "path": path, "sub_date": sd, "sub_time":st, "due_date": dd, "due_time":dt})

    split = x['path'].split('/')
    file_name = ""
    for cur in split:
        file_name = cur

    response = HttpResponse(FileWrapper(open(x['path'])), content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    response['X-Sendfile'] = smart_str(x['path'])
    return response
"""
"""
def getfileAssignments(request):
    val = request.POST['list']
    val = val.replace("'","'")
    y = json.loads(val)

    clss = y['class']
    sec  = y['section']
    assi = y['assignment']
    path = y['path']
    dd = y['due_date']
    dt = y['due_time']

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["student_submissions"]
    mycol = mydb["assignments"]
    x = mycol.find_one({"class": clss, "section": sec, "assignment": assi, "path": path, "due_date": dd, "due_time": dt})
    
    split = x['path'].split('/')
    file_name = ""
    for cur in split:
        file_name = cur

    response = HttpResponse(FileWrapper(open(x['path'])), content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    response['X-Sendfile'] = smart_str(x['path'])
    return response
"""