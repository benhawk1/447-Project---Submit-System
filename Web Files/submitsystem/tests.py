# to test: run {python manage.py test submitsystem} in Web Files
# expected output: "Ran 9 tests in <time> OK"

from django.test import TestCase
from django.urls import reverse
from django.test import Client

# test submitsystem urls, views, and forms
class Iteration1Tests(TestCase):

    # visit login page and enter username and password
    def test_login(self):
        client = Client()
        response = self.client.post(reverse("index"), username="John1", password="Eggs")
        self.assertIs(response.status_code, 200)

    # home page changed

    # visit contact page
    def test_contact(self):
        client = Client()
        response = self.client.get(reverse("contact"))
        self.assertIs(response.status_code, 200)

    # result page removed
    # submit page changed

# tests get method for home, submit, student manager, and assignments page
# tests get method for submit, student manager, and assignments page
class Iteration2Tests(TestCase):

    #  visit home page
    def test_home(self):
        client = Client()
        response = self.client.get(reverse("home"))
        self.assertIs(response.status_code, 200)

    # visit submit page
    def test_submit_get(self):
        client = Client()
        response = self.client.get(reverse("submit"))
        self.assertIs(response.status_code, 200)

    # submit file on submit page
    def test_submit_post(self):
        client = Client()
        response = self.client.post(reverse("submit"), submission=open("submitsystem/uploads/test.txt", "r"))
        self.assertIs(response.status_code, 200)

    # visit student manager page
    def test_studentmanager_get(self):
        client = Client()
        response = self.client.get(reverse("studentmanager"))
        self.assertIs(response.status_code, 200)

    # add student on student manager page
    def test_studentmanager_post(self):
        client = Client()
        response = self.client.post(reverse("studentmanager"), addRemove="Add", classNum=447, section=1,
                                    firstName="Eric", lastName="Hamilton", id="EH999")
        self.assertIs(response.status_code, 200)

    # visit assignments page
    def test_assignments_get(self):
        client = Client()
        response = self.client.get(reverse("assignments"))
        self.assertIs(response.status_code, 200)

    # add assignment on assignments page
    def test_assignments_post(self):
        client = Client()
        response = self.client.post(reverse("assignments"), createRemove="Create", classNum=447, section=1,
                                    assignmentName="HW1", datetimeDue="12/30/2020",
                                    uploadFile=open("submitsystem/uploads/test.txt", "r"))
        self.assertIs(response.status_code, 200)
