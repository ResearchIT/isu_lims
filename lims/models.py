from django.db import models
from django.contrib.auth.models import User
from datetime import date

#admin only
class Accession(models.Model):

    class EAccessionType(models.TextChoices):
        WILD = 'W', 'Wild'
        DOMESTICATED = 'D', 'Domesticated'
        LANDRACE = 'L', 'Landrace'
        UNKNOWN = 'U', 'Unknown'

    accession = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=EAccessionType.choices, blank = True, null = True)
    genus = models.CharField(max_length=200, blank = True)
    subgenus = models.CharField(max_length=200, blank = True)
    genome = models.CharField(max_length=200, blank = True)
    species = models.CharField(max_length=200, blank = True)
    alternatenames = models.CharField(max_length=100, blank = True)
    pinumber = models.CharField(max_length=30, blank = True)
    demoboll = models.BooleanField(null = True)
    collection_location = models.CharField(max_length=200, blank = True)
    # add alternate names
    # add PI-number (USDA germplasm database - could be a link, maybe)

    def __str__(self):
        return ' '.join([self.genus, self.subgenus, self.genome, self.species, self.accession])

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
    accession = models.ForeignKey(Accession, on_delete=models.CASCADE)
    project = models.ManyToManyField(Project)
    fromseedpacket = models.ForeignKey('SeedPacket', on_delete=models.CASCADE, blank = True, null = True)
    location = models.CharField(max_length=200, blank = True)
    flowering = models.BooleanField(null = True)

    def __str__(self):
        return self.accession.genus + ' ' + self.accession.species + ' ' + self.accession.accession

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
    datecollected = models.DateField(blank = True, null = True)
    location = models.CharField(max_length=100, blank = True)
    checkedoutby = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.accession.genus + ' ' + self.accession.species + ' ' + self.accession.accession

class Sample(models.Model):

    class ESampleType(models.TextChoices):
        DNA = 'D', 'DNA'
        RNA = 'R', 'RNA'
        PROTEIN = 'P', 'Protein'
        EPIGENETIC = 'E', 'Epigenetic'
        OTHER = 'O', 'Other'

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, blank = True, null = True)
    project = models.ManyToManyField(Project)
    sample = models.CharField(max_length=200)
    category = models.CharField(max_length=1, choices=ESampleType.choices, null = True)
    notes = models.TextField(blank = True)
    accession = models.ForeignKey(Accession, on_delete=models.CASCADE, blank = True, null = True)
    sequencingcompany = models.CharField(max_length=30, blank = True)
    pcrfree = models.BooleanField(null = True)
    sranumber = models.CharField(max_length=15, blank = True)
    coverage = models.CharField(max_length=15, blank = True)
    strategy = models.CharField(max_length=20, blank = True)
    trackingnumber = models.CharField(max_length=100, blank = True)
    sequenceinstrument = models.CharField(max_length=100, blank = True)
    tissue_type = models.CharField(max_length=200, blank = True, null = True)
    time_point = models.CharField(max_length=200, blank = True)
    dev_time_point = models.CharField(max_length=200, blank = True)
    file_names = models.TextField(blank = True)
    file_location = models.CharField(max_length=200, blank = True)

    def __str__(self):
        return self.sample

class PlantPhoto(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    photo = models.ImageField()

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