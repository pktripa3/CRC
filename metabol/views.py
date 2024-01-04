from django.views.generic import ListView
from django.shortcuts import render
# from django.views.generic import ListView
from django.db.models import Q
from .models import Metabolite_crc

#metabolite view
class metabolite_view(ListView):
    template_name= "metabolite.html"

    def get_queryset(self):
        query = self.request.GET.get("q", default=".")
        object_list = Metabolite_crc.objects.filter(Q(Plant_Name=query))
        return object_list
    