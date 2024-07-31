from django.urls import path
from . import views

app_name = 'websiteapp'

urlpatterns = [
    path("", views.view_mainpage, name="home"),
    path("contact/", views.view_contact, name='contact'),
    path("aboutme/", views.view_aboutme, name="aboutme")
]
