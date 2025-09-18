from django.urls import path
from . import views

urlpatterns = [
    path('to-do-tasks/',views.index, name="index"),
    path('add-new-task/',views.addTask,name="New-Task"),
]