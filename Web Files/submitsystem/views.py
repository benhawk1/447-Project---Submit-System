from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SubmitForm
from submitsystem.submission_backend import submit_file # an ide may complain about this import but it's what django needs to recognize the file

# write submitted file to uploads folder
def handle_uploaded_file(f):
    path = 'submitsystem/uploads/' + f.name
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return path

# log in page
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

def contact(request):
    return render(request, 'submitsystem/contactPage.html')

# home and submit page combined
# @login_required (to be added next iteration)
def home(request):
    # if this is a POST request, process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubmitForm(request.POST, request.FILES)

        # check whether it's valid:
        if form.is_valid():
            # process the file
            path = handle_uploaded_file(request.FILES['submission'])

            # add to db
            submit_file(path, 'student_submissions')

    # if a GET (or any other method) create a blank form
    else:
        form = SubmitForm()

    return render(request, 'submitsystem/homePage.html', {'form': form})

# former submit page
def submit(request):
    return render(request, 'submitsystem/submitPage.html')

# file submission confirmation
def result(request):
    return render(request, 'submitsystem/result.html')
