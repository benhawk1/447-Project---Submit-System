from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.home, name='home'),
    path('submit/', views.submit, name='submit'),
    path('result/', views.result, name='result')
]