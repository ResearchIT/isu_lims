from django.db import models

class Genus(models.Model):
    genus = models.CharField(max_length=200)

class SubGenus(models.Model):
    subgenus = models.CharField
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE)

class Genome(models.Model):
    genome = models.CharField(max_length=200)
    subgenus = models.ForeignKey(SubGenus, on_delete=models.CASCADE)

class Species(models.Model):
    species = models.CharField(max_length=200)
    genome = models.ForeignKey(Genome, on_delete=models.CASCADE)

WILD = 'W'
DOMESTICATED = 'D'
ACCESSION_TYPE_CHOICES = (
    (WILD, 'Wild'),
    (DOMESTICATED, 'Domesticated'),
)
class Accession(models.Model):
    accession = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=ACCESSION_TYPE_CHOICES)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)

class Plant(models.Model):
    notes = models.TextField
    fromseed = models.ForeignKey('Seed', on_delete=models.CASCADE)

class SeedPacket(models.Model):
    notes = models.TextField
    parenta = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='offspringa')
    parentb = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='offspringb')
    quantity = models.IntegerField

class Seed(models.Model):
    notes = models.TextField
    seed_packet = models.ForeignKey(SeedPacket, on_delete=models.CASCADE)

class Project(models.Model):
    name = models.CharField(max_length=200)
    startdate = models.DateField
    enddate = models.DateField
    url = models.URLField

