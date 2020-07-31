from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("cookies/", views.cookies_creation, name = "cookies"),
    path("track/", views.track_user, name = "trackUser"),
    path("home/", views.home_page, name = "home_page"),
    path("delete_cookie", views.delete_cookie, name = "deleteTheCookie" )
]