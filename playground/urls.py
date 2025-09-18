from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
    path("",views.say_hi),
    path('hello/',views.hello),
    path('<str:name>',views.greet),
]