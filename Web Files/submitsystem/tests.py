# to test: run {python manage.py test submitsystem} in Web Files
# expected output: "Ran 9 tests in <time> OK"

from django.test import TestCase
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User

# user that will be logged in for the majority of tests
client = Client()

# tests login and page restriction, run before the other iterations' test to include a user that is not logged in yet
class Iteration3Tests(TestCase):

    #  try to vist home page without logging in
    def test_not_logged_in(self):
        client = Client()
        response = client.get(reverse("home"))
        self.assertEqual(response.status_code, 302)

    # login (this will allow the client to be logged in for the rest of the tests)
    def test_logged_in(self):
        response = client.post(reverse("index"), username="John1", password="Eggs")
        self.assertEqual(response.status_code, 200)

# test student: home, contact, submit, and assignments page
class Iteration4Tests(TestCase):

    #  visit student home page
    def test_home(self):
        response = client.get(reverse("studenthome"))
        self.assertEqual(response.status_code, 302)

    # visit student contact page
    def test_contact(self):
        response = client.get(reverse("studentcontact"))
        self.assertEqual(response.status_code, 302)

    # visit student submit page
    def test_submit_get(self):
        response = client.get(reverse("studentsubmit"))
        self.assertEqual(response.status_code, 302)

    # submit file on student submit page
    def test_submit_post(self):
        response = client.post(reverse("studentsubmit"), studentClass=447, section=1, assignment="HW1", submission=open("submitsystem/uploads/test.txt", "r"))
        self.assertEqual(response.status_code, 302)

    # visit student assignments page
    def test_assignments(self):
        response = client.get(reverse("studentassignments"))
        self.assertEqual(response.status_code, 302)

# test submitsystem urls, views, and forms
class Iteration1Tests(TestCase):

    # login page changed
    # home page changed

    # visit contact page
    def test_contact(self):
        response = client.get(reverse("contact"))
        self.assertEqual(response.status_code, 302)

    # result page removed
    # submit page changed

# tests get method for home, submit, student manager, and assignments page
# tests post method for submit, student manager, and assignments page
class Iteration2Tests(TestCase):

    #  visit home page
    def test_home(self):
        response = client.get(reverse("home"))
        self.assertEqual(response.status_code, 302)

    # visit submit page
    def test_submit_get(self):
        response = client.get(reverse("submit"))
        self.assertEqual(response.status_code, 302)

    # submit file on submit page
    def test_submit_post(self):
        response = client.post(reverse("submit"), submission=open("submitsystem/uploads/test.txt", "r"))
        self.assertEqual(response.status_code, 302)

    # visit student manager page
    def test_studentmanager_get(self):
        response = client.get(reverse("studentmanager"))
        self.assertEqual(response.status_code, 302)

    # add student on student manager page
    def test_studentmanager_post(self):
        response = client.post(reverse("studentmanager"), addRemove="Add", classNum=447, section=1,
                                    firstName="Eric", lastName="Hamilton", id="EH999")
        self.assertEqual(response.status_code, 302)

    # visit assignments page
    def test_assignments_get(self):
        response = client.get(reverse("assignments"))
        self.assertEqual(response.status_code, 302)

    # add assignment on assignments page
    def test_assignments_post(self):
        response = client.post(reverse("assignments"), createRemove="Create", classNum=447, section=1,
                                    assignmentName="HW1", datetimeDue="12/30/2020",
                                    uploadFile=open("submitsystem/uploads/test.txt", "r"))
        self.assertEqual(response.status_code, 302)

