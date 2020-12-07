# forms for getting data from html pages

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import InlineCheckboxes, InlineRadios

# get username and password on login page
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# get file submission from home page
class StudentSubmitForm(forms.Form):
    sectionChoices = []
    classChoices=[('cmsc447', 'CMSC 447'), ('cmpe315', 'CMPE 315')]
    assignmentNames=[('homework1', 'Homework 1'), ('lab4', 'Lab 4')]
    sectionChoices=[('section1', 'Section 1'), ('section3', 'Section 3')]
    studentClass = forms.CharField(label='Class:',widget=forms.Select(choices=classChoices))
    section = forms.CharField(label='Section:',widget=forms.Select(choices=sectionChoices))
    submission = forms.FileField(label='')
    assignment = forms.CharField(label='Assignment', widget=forms.Select(choices=assignmentNames))

# get file submission from home page
class SubmitForm(forms.Form):
    sectionChoices = []
    classChoices=[('cmsc447', 'CMSC 447'), ('cmsc341', 'CMSC 341')]
    assignmentNames=[('homework1', 'Homework 1'), ('project2', 'Project 2')]
    sectionChoices=[('section1', 'Section 1'), ('section2', 'Section 2')]
    studentClass = forms.CharField(label='Class:',widget=forms.Select(choices=classChoices))
    section = forms.CharField(label='Section:',widget=forms.Select(choices=sectionChoices))
    submission = forms.FileField(label='')
    assignment = forms.CharField(label='Assignment', widget=forms.Select(choices=assignmentNames))

# get student data to add or remove from student management page
class StudentForm(forms.Form):
    addRemove = forms.ChoiceField(choices=[("Add", "Add"), ("Remove", "Remove")])
    classNum = forms.CharField()
    sectionChoices = []
    for i in range(1, 5):
        sectionChoices.append((i, f'Section {i}'))
    #section = forms.ChoiceField(choices=sectionChoices)
    section = forms.ChoiceField(widget=forms.RadioSelect,choices=sectionChoices)
    firstName = forms.CharField()
    lastName = forms.CharField()
    id = forms.CharField()
    #email = forms.CharField(widget=forms.EmailInput, required=False) replaced with id
    #roster = forms.FileField(label='', required=False) not yet supported
    helper = FormHelper()
    helper.layout = Layout(InlineRadios('section'))

class AssignmentForm(forms.Form):
    createRemove = forms.ChoiceField(choices=[("Create", "Create"), ("Remove", "Remove")])
    classNum = forms.CharField()
    sectionChoices = []
    for i in range(1, 5):
        sectionChoices.append((i, f'Section {i}'))
    #section = forms.ChoiceField(choices=sectionChoices)
    section = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=sectionChoices)
    assignmentName = forms.CharField()
    datetimeDue = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    uploadFile = forms.FileField(label='')
    helper = FormHelper()
    helper.layout = Layout(InlineCheckboxes('section'))
