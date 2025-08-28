from django.contrib import admin
from django.urls import path, include
from .views import hellow_world

urlpatterns = [
    path("hello/", hellow_world),
]
