from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('game/<int:pk>', views.game_page),
    path('login', views.login, name = "login")
]