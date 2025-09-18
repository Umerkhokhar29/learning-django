from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
def home(request):
    return render(request,'index.html')
def say_hi(request):
    return HttpResponse("Hi Django")
def calculate():
    x = 5
    y = 44
    return x * y/2
def checkDate():
    current_date = datetime.today()
    date = int(current_date.strftime("%d"))
    return {"date":date,
            "current_date":current_date}
def hello(request):
    x = calculate()
    name = None
    if request.method == "POST":
        name = request.POST.get("fname")
    return render(request,'hello.html',{'name':name, "x":x})

def greet(request,name):
    date_dict = {}
    date_dict = checkDate()
    return render(request, 'greet.html',{
                  "name":name.capitalize(),
                  "date":date_dict.get("date"),
                  "current_date": date_dict.get("current_date"),
                   })
# Create your views here.
