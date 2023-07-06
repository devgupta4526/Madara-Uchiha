from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from courses.models import Course , Video
from django.contrib.auth.forms import UserCreationForm
from courses.forms import RegistrationForm
from courses.forms import RegistrationForm , LoginForm
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth import logout , login
from django.urls import reverse



class SignupView(View):
    def get(self, request):
         form = RegistrationForm()
         return render(request , template_name="courses/signup.html", context={"form" : form})

    def post(self , request):
        form = RegistrationForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            print(user.first_name)
            if(user is not None):
                return redirect(reverse("courses:login"))

        return render(request , template_name="courses/signup.html", context={"form" : form})



class LoginView(View):
    def get(self,request):
        form = LoginForm()
        context = {
            "form" : form
        }
        return render(request , template_name="courses/login.html", context= context)
    
    def post(self,request):
        form = LoginForm(request = request ,data= request.POST)
        context = {
            "form" : form
        }
        if(form.is_valid()):
             return redirect("home")
        return render(request , template_name="courses/login.html", context= context)



    

def signout(request ):
    logout(request)
    return redirect("home")