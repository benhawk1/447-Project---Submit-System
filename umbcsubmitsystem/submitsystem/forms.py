from django import forms

class SubmitForm(forms.Form):
    submission = forms.FileField(label='')

class TestForm(forms.Form):
    name = forms.CharField()