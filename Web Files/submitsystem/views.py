from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SubmitForm, StudentForm, AssignmentForm
from submitsystem.submission_backend import *
from submitsystem.db_func import *
from submitsystem.section_management import *
from django.views.generic.base import TemplateView

# write submitted file to uploads folder
def handle_uploaded_file(f):
    path = 'submitsystem/uploads/' + f.name
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return path

# login page
def index(request):
    # if this is a POST request, process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = LoginForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # process the input
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # assume correct login for now and redirect to home page
            return HttpResponseRedirect('home/')

    # if a GET (or any other method) create a blank form
    else:
        form = LoginForm()

    return render(request, 'submitsystem/loginPage.html', {'form': form})

# contact page
def contact(request):
    return render(request, 'submitsystem/contactPage.html')

# submit page
# @login_required (to be added next iteration)
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

            # add sample course, section, and student (expected to say collection create failed if course already exits)
            create_collection('CMSC 447')
            add_section(5, 'CMSC 447')
            add_student("EH999", "Eric Hamilton", 5, 'CMSC 447')

            # add to db
            submit_file("EH999", 5, path, 'CMSC 447') # using sample student id and section for now

            # add message to display to user
            fileSubmitted = "File submitted"

    # if a GET (or any other method) create a blank form
    else:
        form = SubmitForm()

    return render(request, 'submitsystem/submissionPage.html', {'form': form, 'fileSubmitted' : fileSubmitted})

# student manager page
# @login_required (to be added next iteration)
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
            print(addRemove, classNum, section, firstName, lastName, id)

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
# @login_required (to be added next iteration)
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

            print(createRemove, classNum, section, assignmentName, datetimeDue)

            # add course and section(s) # (expected to say collection create failed if course already exits)
            create_collection(classNum)
            add_section(section, classNum)
            # create assignment or remove assignment if create is not selected
            if createRemove == "Create":
                add_assignment(section, path, datetimeDue, classNum)
                assignmentAction = "Assignment Successfully Created"
            else:
                remove_assignment(section, path, classNum)
                assignmentAction = "Assignment Successfully Removed"


    # if a GET (or any other method) create a blank form
    else:
        form = AssignmentForm()

    return render(request, 'submitsystem/AssignmentPage.html', {'form' : form, 'assignmentAction' : assignmentAction})

# Home Page table:
# @login_required (to be added next iteration)
class homeTable(TemplateView):
    template_name = 'submitsystem/newHomePage.html'

    def get_context_data(self, **kwargs):
        context = super(homeTable, self).get_context_data(**kwargs)
        context["rosterhead"] = ['Class Number', 'Section', 'First Name', 'Last Name', 'E-Mail']
        context["rosterbody"] = [{'classname':1, 'section':1, 'firstname':'John', 'lastname':'Lewis', 'email':'john1@umbc.edu'},
                                 {'classname':2, 'section':2, 'firstname':'Will', 'lastname':'Greene', 'email':'Greene@umbc.edu'}
                                 ]
        return context
    
