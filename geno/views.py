from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from .models import Genome_crc
    
    #genome view
class genome_view(ListView):
        template_name= "genome.html"
    
        def get_queryset(self):
            query = self.request.GET.get("q", default="1")
            object_list = Genome_crc.objects.filter(Q(GeneID=query))
            return object_list