from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('submit/', views.submit, name='submit'),
    path('result/', views.result, name='result'),
    url('home/', views.homeTable.as_view(), name='home') #replaces: path('home/', views.home, name='home'),
]