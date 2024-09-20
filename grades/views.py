from django.shortcuts import render
from django.http import HttpResponse
from .models import gradesystem
# Create your views here.
def grades(request):
    data=gradesystem.objects.all()
    grading={
        'data':data
    }
    return render(request,'stugrades.html',context=grading)
    
    
def grade(request):
    return render(request,('signup.html'))

def studentgrading(request):
    data= gradesystem.objects.all()
    print('Data From Products Table',data)
    stugrading={
        'data': data
    }
    return render(request,'stugrades.html',context=stugrading)
    