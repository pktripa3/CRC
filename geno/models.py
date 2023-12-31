from django.db import models
from django.db import connections 

# Create your models here.
class Genome_crc(models.Model):
    tax_id = models.IntegerField()
    Org_name = models.TextField()
    GeneID = models.IntegerField()
    CurrentID = models.IntegerField()
    Status = models.TextField()
    Symbol = models.TextField()
    Aliases = models.TextField()
    description = models.TextField()
    other_designations = models.TextField()
    map_location = models.IntegerField()
    chromosome = models.TextField()
    genomic_nucleotide_accession = models.TextField()
    start_position_on_the_genomic_accession = models.IntegerField()
    end_position_on_the_genomic_accession = models.IntegerField()
    orientation	= models.TextField()
    exon_count = models.IntegerField()	
    OMIM = models.IntegerField()