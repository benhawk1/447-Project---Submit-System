from django import forms

# get username and password on login page
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# get file submission from home page
class SubmitForm(forms.Form):
    submission = forms.FileField(label='')
