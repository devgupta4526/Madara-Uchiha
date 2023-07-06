from django.shortcuts import render
from portfolio.views import home
from portfolio.models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio.html", {"projects": projects})
