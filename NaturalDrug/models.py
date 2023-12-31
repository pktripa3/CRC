from django.db import models
from django.db import connections 

# Create your models here.
class Drug_crc(models.Model):
    Drug_ID_MESH = models.IntegerField()
    Drug = models.CharField(max_length=200)
    Source_Plant = models.TextField()
    Mechanism_of_action = models.TextField()
    chemical_structure = models.URLField()
    PMID = models.IntegerField()