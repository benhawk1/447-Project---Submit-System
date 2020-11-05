# forms for getting data from html pages

from django import forms

# get username and password on login page
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# get file submission from home page
class SubmitForm(forms.Form):
    submission = forms.FileField(label='')

# get student data to add or remove from student management page
class StudentForm(forms.Form):
    addRemove = forms.ChoiceField(choices=[("Add", "Add"), ("Remove", "Remove")], required=False)
    classNum = forms.IntegerField(required=False)
    sectionChoices = []
    for i in range(1, 5):
        sectionChoices.append((i, f'Section {i}'))
    section = forms.ChoiceField(widget=forms.RadioSelect(attrs={"class" : "radio-inline"}), choices=sectionChoices, required=False)
    firstName = forms.CharField(required=False)
    lastName = forms.CharField(required=False)
    id = forms.CharField()
    #email = forms.CharField(widget=forms.EmailInput, required=False)
    #roster = forms.FileField(label='', required=False)

class AssignmentForm(forms.Form):
    createRemove = forms.ChoiceField(choices=[("Create", "Create"), ("Remove", "Remove")], required=False)
    classNum = forms.IntegerField(required=False)
    sectionChoices = []
    for i in range(1, 5):
        sectionChoices.append((i, f'Section {i}'))
    section = forms.MultipleChoiceField(widget=forms.RadioSelect(attrs={"class": "radio-inline"}), choices=sectionChoices, required = False)
    assignmentName = forms.CharField(required=False)
    datetimeDue = forms.DateTimeField(required=False)
