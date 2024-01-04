from django.views.generic import ListView
from django.shortcuts import render
# from django.views.generic import ListView
from django.db.models import Q
from .models import fam_crc
#genome view
class fam_view(ListView):
    template_name= "family.html"

    def get_queryset(self):
        query = self.request.GET.get("q", default=".")
        object_list = fam_crc.objects.filter(Q(Plant_common_name=query))
        return object_list
    