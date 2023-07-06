from django.shortcuts import render
from django.shortcuts import HttpResponse
from courses.models import Course

def home(request):
    courselist = Course.objects.all()
    return render(request , "courses/home.html" ,{"courses": courselist})
