from django.db import models
from django.contrib.auth.models import User
from datetime import date
import enum

class Genus(models.Model):
    genus = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Genera"
    
    def __str__(self):
        return self.genus

class Subgenus(models.Model):
    subgenus = models.CharField(max_length=200, blank = True)
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE, blank = True, null = True)
    
    class Meta:
        verbose_name_plural = "SubGenera"

    def __str__(self):
        return self.subgenus

class Genome(models.Model):
    genome = models.CharField(max_length=200, blank = True)
    subgenus = models.ForeignKey(Subgenus, on_delete=models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.genome

class Species(models.Model):
    species = models.CharField(max_length=200, blank = True)
    genome = models.ForeignKey(Genome, on_delete=models.CASCADE, blank = True, null = True)

    class Meta:
        verbose_name_plural = "Species"
    
    def __str__(self):
        return self.species



#admin only
class Accession(models.Model):

    class EAccessionType(enum.Enum):
        WILD = 'W'
        DOMESTICATED = 'D'
        LANDRACE = 'L'
        UNKNOWN = 'U'

    ACCESSION_TYPE_CHOICES = (
        (EAccessionType.WILD.value, 'Wild'),
        (EAccessionType.DOMESTICATED.value, 'Domesticated'),
        (EAccessionType.LANDRACE.value, 'Landrace'),
        (EAccessionType.UNKNOWN.value, 'Unknown'),
    )

    accession = models.CharField(max_length=200, blank = True)
    status = models.CharField(max_length=1, choices=ACCESSION_TYPE_CHOICES, blank = True, null = True)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, blank = True, null = True)
    alternatenames = models.CharField(max_length=100, blank = True)
    pinumber = models.CharField(max_length=30, blank = True)
    # add alternate names
    # add PI-number (USDA germplasm database - could be a link, maybe)

    def __str__(self):
        return self.accession

# needs to relate to plants & samples too
class Project(models.Model):
    project = models.CharField(max_length=200, blank = True)
    startdate = models.DateField(auto_now_add = False, null = True, blank = True)
    enddate = models.DateField(auto_now_add = False, null = True, blank = True)
    url = models.URLField(blank = True, null = True)
    grantnumber = models.TextField(blank = True)
    grantagency = models.TextField(blank = True)
    lead = models.CharField(max_length=100, blank = True)

    def __str__(self):
        return self.project

# needs a form to create
# relates to sample
# needs sample dates
# needs a disposition 
# flowering or not
class Plant(models.Model):
    notes = models.TextField(blank = True)
    accession = models.ForeignKey(Accession, on_delete=models.CASCADE, blank = True, null = True)
    project = models.ManyToManyField(Project)
    fromseedpacket = models.ForeignKey('SeedPacket', on_delete=models.CASCADE, blank = True, null = True)
    location = models.CharField(max_length=200, blank = True)
    flowering = models.BooleanField(null = True)

    def __str__(self):
        return self.accession.species.genome.subgenus.genus + ' ' + self.accession.species + ' ' + self.accession.accession

# need to track who has them checked out / location (box, or desk, or storage, etc.)
# should be in storage, but often kept at workbench
# sending to collaborators
# what did they do with the seeds ? (sample, planted, etc.)
# might get shipped & not be part of collection at all anymore
class SeedPacket(models.Model):
    accession = models.ForeignKey(Accession, on_delete=models.CASCADE)
    notes = models.TextField(blank = True)
    parenta = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='offspringa', blank = True, null = True)
    parentb = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='offspringb', blank = True, null = True)
    quantity = models.IntegerField(default=0)
    datecollected = models.DateField(blank = True)
    location = models.CharField(max_length=100, blank = True)
    checkedoutby = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.accession.species.genome.subgenus.genus + ' ' + self.accession.species + ' ' + self.accession.accession

class Sample(models.Model):

    class ESampleType(enum.Enum):
        DNA = 'D'
        RNA = 'R'
        PROTEIN = 'P'
        EPIGENETIC = 'E'
        OTHER = 'O'

    SAMPLE_TYPE_CHOICES = (
        (ESampleType.DNA.value, 'DNA'),
        (ESampleType.RNA.value, 'RNA'),
        (ESampleType.PROTEIN.value, 'Protein'),
        (ESampleType.EPIGENETIC.value, 'Epigenetic'),
        (ESampleType.OTHER.value, 'Other'),
    )

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, blank = True, null = True)
    project = models.ManyToManyField(Project)
    sample = models.CharField(max_length=200, blank = True, null = True)
    category = models.CharField(max_length=1, choices=SAMPLE_TYPE_CHOICES, null = True)
    notes = models.TextField(blank = True)
    accession = models.ForeignKey(Accession, on_delete=models.CASCADE, blank = True, null = True)
    sequencingcompany = models.CharField(max_length=30, blank = True)
    pcrfree = models.BooleanField(null = True)
    sranumber = models.CharField(max_length=15, blank = True)
    coverage = models.CharField(max_length=15, blank = True)
    strategy = models.CharField(max_length=20, blank = True)
    trackingnumber = models.CharField(max_length=100, blank = True)
    sequenceinstrument = models.CharField(max_length=100, blank = True)

    def __str__(self):
        return self.sample

class PlantPhoto(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    photo = models.ImageField(blank = True)

class Herbarium(models.Model):
    barcode = models.IntegerField(primary_key=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    photo = models.ImageField()
    collector = models.CharField(max_length=200)

#sequencing tech
#sequencing center
#sequencing company
#sequencing tracking number
#sra
#pcr free or not
#coverage
#strategy (paired or single) pe-150,se-150, .etc.