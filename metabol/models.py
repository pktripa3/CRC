from django.db import models
from django.db import connections 

# Create your models here.
class Metabolite_crc(models.Model):
    Plant_Name = models.CharField(max_length=200)
    Metabolites = models.CharField(max_length=100)
    Pathway = models.TextField()
    References = models.URLField()
    Citation = models.TextField()