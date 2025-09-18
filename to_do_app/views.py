from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task: ", required=True)
    priority = forms.IntegerField(label="Add Priority", required=True,min_value=1, max_value=10)
 
def addTask(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST) 
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["listOfTask"] += [task]
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "tasks/add.html",{
                "form" : form
            })
    return render(request,"tasks/add.html",
                  {"form": NewTaskForm()
    })
listOfTask = []

def index(request):
    if "listOfTask" not in request.session:
        request.session["listOfTask"] = []

    return render(request,"tasks/index.html",{
        "listOfTask":request.session["listOfTask"],
    })
# Create your views here.
