from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, "partials/home.html", {"projects": projects})


def layout(request):
    projects = Project.objects.all()
    return render(request, "partials/layout.html", {"projects": projects})

def navbar(request):
    projects = Project.objects.all()
    return render(request, "navbar.html", {"projects": projects})
