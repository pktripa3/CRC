from django.db import models
from django.db import connections 

# Create your models here.
class Metabolo_crc(models.Model):
    Plant_Name = models.TextField()
    Scientific_Name = models.TextField()
    Family = models.TextField()
    Metabolites = models.CharField(max_length=100)
    Pathway = models.TextField()
    References = models.URLField()