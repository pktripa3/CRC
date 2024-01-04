from django.views.generic import ListView
from django.shortcuts import render
# from django.views.generic import ListView
from django.db.models import Q
from .models import Drug_crc

#drugview
class drug_view(ListView):
    template_name= "drug.html"

    def get_queryset(self):
        query = self.request.GET.get("q", default=".")
        object_list = Drug_crc.objects.filter(Q(Drug=query))
        return object_list
    