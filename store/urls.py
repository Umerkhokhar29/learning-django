from django.urls import path
from . import views

urlpatterns = [
    path("",views.checkApp,name="demo"),
]
