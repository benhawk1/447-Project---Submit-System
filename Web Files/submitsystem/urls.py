from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
#    path('<str:filepath>/', views.download_file),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('submit/', views.submit, name='submit'),
    path('studentmanager/', views.studentmanager, name='studentmanager'),
    path('assignments/', views.assignments, name="assignments"),
    url('home/', views.homeTable.as_view(), name='home'),
]