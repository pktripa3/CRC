from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render (request, "home.html", {})

def about_view(request, *args, **kwargs):
    return render (request, "about.html", {})

def contact_view(request, *args, **kwargs):
    return render (request, "contact.html", {})

def factors_view(request, *args, **kwargs):
    return render (request, "factors.html", {})

def role_view(request, *args, **kwargs):
    return render (request, "role.html", {})

def stages_view(request, *args, **kwargs):
    return render (request, "stages.html", {})


def medical_view(request, *args, **kwargs):
    return render (request, "medical.html", {})
