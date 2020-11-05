from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SubmitForm
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

            # add sample section and student
            add_section(5, 'sections_test')
            add_student("12345", "Queen Victoria", 5, 'sections_test')

            # add to db
            submit_file("12345", 5, path, 'sections_test', ) # using sample student id and section for now

            # add message to display to user
            fileSubmitted = "File submitted"

    # if a GET (or any other method) create a blank form
    else:
        form = SubmitForm()

    return render(request, 'submitsystem/submissionPage.html', {'form': form, 'fileSubmitted' : fileSubmitted})

# file submission confirmation (depreciated)
def result(request):
    return render(request, 'submitsystem/result.html')

# Home Page table:
class homeTable(TemplateView):
    template_name = 'submitsystem/newHomePage.html'

    def get_context_data(self, **kwargs):
        context = super(homeTable, self).get_context_data(**kwargs)
        context["rosterhead"] = ['Class Number', 'Section', 'First Name', 'Last Name', 'E-Mail']
        context["rosterbody"] = [{'classname':1, 'section':1, 'firstname':'John', 'lastname':'Lewis', 'email':'john1@umbc.edu'},
                                 {'classname':2, 'section':2, 'firstname':'Will', 'lastname':'Greene', 'email':'Greene@umbc.edu'}
                                 ]
        return context
    
