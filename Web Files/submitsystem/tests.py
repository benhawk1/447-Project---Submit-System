# to test: run {python manage.py test submitsystem} in Web Files
# expected output: "Ran 5 tests in <time> OK"

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

    #  visit home page and submit file
    def test_home(self):
        client = Client()
        response = self.client.post(reverse("home"), submission=open("submitsystem/uploads/test.txt", "r"))
        self.assertIs(response.status_code, 200)

    # visit contact page
    def test_contact(self):
        client = Client()
        response = self.client.get(reverse("contact"))
        self.assertIs(response.status_code, 200)

    # visit submit page
    def test_submit(self):
        client = Client()
        response = self.client.get(reverse("submit"))
        self.assertIs(response.status_code, 200)

    # visit result page
    def test_result(self):
        client = Client()
        response = self.client.get(reverse("result"))
        self.assertIs(response.status_code, 200)

