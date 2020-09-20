from django.contrib import admin
from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.index),
    path('createtask', views.createtask),
    path('deletetasks', views.deletetasks),
    path('makereq', views.makereq)
]

##
