"""
URL configuration for colorectal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from geno.views import GenomeView
from NaturalDrug.views import drug_view
from metabolo.views import metabolo_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from phase.views import home_view, about_view, contact_view, medical_view, factors_view, role_view, stages_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('home.html', home_view ,name="home"),
    path ('about.html', about_view ,name="about"),
    path ('contact.html', contact_view ,name="contact"),
    path ('medical.html', medical_view ,name="medical"),
    path ('factors.html', factors_view ,name="factors"),
    path ('role.html', role_view ,name="role"),
    path ('stages.html', stages_view ,name="stages"),
    path('genome.html', GenomeView.as_view(), name="genome"),
    path('drug.html', drug_view.as_view(), name="drug"),
    path('metabolo.html', metabolo_view.as_view(), name="metabolite"),
    path('genome/',GenomeView.as_view() ,name='genome'),
    path('genome/',drug_view.as_view() ,name='drug'),
    path('genome/',metabolo_view.as_view() ,name='metabolite'),
    path('home/about.html',about_view,name='about'),
    path('home/home.html',home_view,name='home'),
    path('home/genome.html',GenomeView.as_view(),name='genome'),
    path('home/drug.html',drug_view.as_view(),name='drug'),
    path('home/metabolo.html',metabolo_view.as_view(),name='metabolite'),

    path('',home_view)       
]

urlpatterns += staticfiles_urlpatterns()
