from django.db import models
from django.db import connections 

# Create your models here.
class fam_crc(models.Model):
    Plant_common_name = models.TextField()
    Scientific_Name = models.TextField()
    Family = models.TextField()
   
