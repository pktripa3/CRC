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
from geno.views import genome_view
from NaturalDrug.views import drug_view
from fam.views import fam_view
from metabol.views import metabolite_view
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
    path('genome.html', genome_view.as_view(), name="genome"),
    path('drug.html', drug_view.as_view(), name="drug"),
    path('family.html', fam_view.as_view(), name="family"),
    path('metabolite.html', metabolite_view.as_view(), name="metabolite"),
    path('genome/',genome_view.as_view() ,name='genome'),
    path('genome/',drug_view.as_view() ,name='drug'),
    path('genome/',fam_view.as_view() ,name='family'),
    path('genome/',metabolite_view.as_view() ,name='metabolite'),
    path('home/about.html',about_view,name='about'),
    path('home/home.html',home_view,name='home'),
    path('home/genome.html',genome_view.as_view(),name='genome'),
    path('home/drug.html',drug_view.as_view(),name='drug'),
    path('home/family.html',fam_view.as_view(),name='family'),
    path('home/metabolite.html',metabolite_view.as_view(),name='metabolite'),

    path('',home_view)       
]

urlpatterns += staticfiles_urlpatterns()
