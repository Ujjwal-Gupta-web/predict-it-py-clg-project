from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index , name="home"),
    path("list_cars",views.list_cars , name="list_cars"),
    path("browse",views.browse , name="browse"),
    path("signup",views.handleSignup , name="handleSignup"),
    path("login",views.handleLogin , name="handleLogin"),
    path("logout",views.handleLogout , name="handleLogout"),
    path("dashboard",views.dashboard , name="dashboard"),
]
