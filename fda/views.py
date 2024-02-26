from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from .models import Fda_crc

# Genome view
class Fdaview(ListView):
    template_name = "fda.html"
    model = Fda_crc  # Specify the model for the ListView

    def get_queryset(self):
        query = self.request.GET.get("q", default="1")
        object_list = Fda_crc.objects.filter(Q(Drug=query))
        return object_list