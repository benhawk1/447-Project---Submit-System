from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('submit/', views.submit, name='submit'),
    path('studentmanager/', views.studentmanager, name='studentmanager'),
    path('assignments/', views.assignments, name="assignments"),
    path('studenthome/', views.studentHome, name='studenthome'),
    path('studentcontact/', views.studentContact, name='studentcontact'),
    path('studentsubmit/', views.studentSubmit, name='studentsubmit'),
    path('studentassignments/', views.studentAssignments, name="studentassignments"),
    path('submissionviewer/', views.submissionViewer, name='submissionViewer'),
    url('home/', views.homeTable.as_view(), name='home'),
]