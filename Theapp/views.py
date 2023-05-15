from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hithere(request):
    return HttpResponse("Hello there Manuel")

def evenodd(request):
    x = 25
    if x%2==0:
        return HttpResponse("Number is even")
    else:
        return HttpResponse("Number is odd")

def index(request):
    return render(request,'index.html')

def table(request):
    return render(request,'tables.html')

def table2(request):
    return render(request,'table2.html')
def variables(request):
    details= {
        "firstname":"Manuel",
        "lastname":"eMobilis",
        "age": 60,
        "place":"Westlands",
    }
    return render(request,'variables.html',details)

def employee(request):
    info={
        "empname":"Manuel",
        "empsalary":50000,
        "empid":101,
    }
    return render(request,'employee.html',info)

def images(request):
    return render(request,'images.html')

def background(request):
    return render(request, 'background.html')