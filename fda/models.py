from django.db import models
from django.db import connections 

# Create your models here.
class Fda_crc(models.Model):
    Drug = models.TextField()
    Genes = models.TextField()
  