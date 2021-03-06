from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from submitsystem.login import loginValidation
import pandas as pd


class SettingsBackend(BaseBackend):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = '01234567'
    """

    def authenticate(self, request, username=None, password=None):
        print(username)
        print(password)
        login_valid = loginValidation(username, password)
        if login_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                df = pd.read_csv("submitsystem/Users.csv")
                rowNumber = int(df[df['Username'] == username].index[0])
                role = df.at[rowNumber, 'Role']
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=username)
                if role == 'P':
                    user.is_staff = True
                else:
                    user.is_staff = False
                user.is_superuser = False
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
