from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SubmitForm
from submitsystem.submission_backend import submit_file # an ide may complain about this import but it's what django needs to recognize the file

def handle_uploaded_file(f):
    path = 'submitsystem/uploads/' + f.name
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return path

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubmitForm(request.POST, request.FILES)

        # check whether it's valid:
        if form.is_valid():
            # process the file
            path = handle_uploaded_file(request.FILES['submission'])

            # add to db
            submit_file(path)

            # redirect to a new URL:
            return HttpResponseRedirect('result/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubmitForm()

    return render(request, 'submitsystem/homePage.html', {'form': form})


def home(request):
    return render(request, 'submitsystem/oldHomePage.html')

def submit(request):
    return render(request, 'submitsystem/submitPage.html')

def result(request):
    return render(request, 'submitsystem/result.html')
