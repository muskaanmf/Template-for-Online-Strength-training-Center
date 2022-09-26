from unicodedata import name
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contacts", views.contacts, name='contacts'),
    path("offers", views.offers, name='offers'),
    path("signup",views.signup, name='signup' ),
    path("signin",views.signin, name='signin'),
    path("purchase",views.purchase, name='purchase'),

]
