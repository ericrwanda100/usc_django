"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('room',views.room, name='room'),
    path('about',views.about, name='about'),
    path('events',views.events, name='events'),
    path('create-room', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('poland',views.poland, name='poland'),
    path('excreate', views.excreate, name='excreate'),
    path('exupdate/<str:pk>/', views.exupdate, name='exupdate'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('logout', views.logoutUser, name='logout'),
    path('loginNow',views.loginNow, name='loginNow'),
    path('register',views.registerPage,name='register'),
    path('gallery', views.gallery, name='gallery'),
    path('roomtwo',views.roomtwo, name='roomtwo'),
    path('usa',views.usa, name='usa'),
    path('canada',views.canada, name='canada'),
    path('loginweek', views.loginweek, name='loginweek'),
    path('otherUniversity', views.otherUniversity, name='otherUniversity'),
]
