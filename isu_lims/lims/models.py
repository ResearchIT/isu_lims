from django.db import models
from datetime import date

class Genus(models.Model):
    genus = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Genera"
    
    def __str__(self):
        return self.genus

class Subgenus(models.Model):
    subgenus = models.CharField(max_length=200, blank = True)
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE, blank = True)
    
    class Meta:
        verbose_name_plural = "SubGenera"

    def __str__(self):
        return self.subgenus

class Genome(models.Model):
    genome = models.CharField(max_length=200, blank = True)
    subgenus = models.ForeignKey(Subgenus, on_delete=models.CASCADE, blank = True)

    def __str__(self):
        return self.genome

class Species(models.Model):
    species = models.CharField(max_length=200, blank = True)
    genome = models.ForeignKey(Genome, on_delete=models.CASCADE, blank = True)

    class Meta:
        verbose_name_plural = "Species"
    
    def __str__(self):
        return self.species

WILD = 'W'
DOMESTICATED = 'D'
LANDRACE = 'L'
UNKNOWN = 'U'
ACCESSION_TYPE_CHOICES = (
    (WILD, 'Wild'),
    (DOMESTICATED, 'Domesticated'),
    (LANDRACE, 'Landrace'),
    (UNKNOWN, 'Unknown'),
)

#admin only
class Accession(models.Model):
    accession = models.CharField(max_length=200, blank = True)
    type = models.CharField(max_length=1, choices=ACCESSION_TYPE_CHOICES, blank = True)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, blank = True)
    # add alternate names
    # add PI-number (USDA germplasm database - could be a link, maybe)

    def __str__(self):
        return self.accession

# needs a form to create
# relates to sample
# needs sample dates
# needs a disposition 
# flowering or not
class Plant(models.Model):
    notes = models.TextField(blank = True)
    fromseed = models.ForeignKey('Seed', on_delete=models.CASCADE, blank = True)
    location = models.CharField(max_length=200, blank = True)
    photo = models.ImageField(blank = True)

    def __str__(self):
        return self.id 

# need to track who has them checked out / location (box, or desk, or storage, etc.)
# should be in storage, but often kept at workbench
# sending to collaborators
# what did they do with the seeds ? (sample, planted, etc.)
# might get shipped & not be part of collection at all anymore
class SeedPacket(models.Model):
    notes = models.TextField(blank = True)
    parenta = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='offspringa', blank = True, null = True)
    parentb = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='offspringb', blank = True, null = True)
    quantity = models.IntegerField(default=0)
    datecollected = models.DateField(blank = True)
    accession = models.ForeignKey(Accession, on_delete=models.CASCADE, blank = True)

    def __str__(self):
        return self.id

# maybe more for hufford lab
class Seed(models.Model):
    notes = models.TextField(blank = True)
    seed_packet = models.ForeignKey(SeedPacket, on_delete=models.CASCADE, blank = True)

    def __str__(self):
        return self.id

# needs to relate to plants & samples too
class Project(models.Model):
    project = models.CharField(max_length=200, blank = True)
    startdate = models.DateField(auto_now_add = True, null = True, blank = True)
    enddate = models.DateField(auto_now_add = True, null = True, blank = True)
    url = models.URLField(blank = True, null = True)
    grant = models.TextField(blank = True)
    # need agency & grant number
    lead = models.CharField(max_length=100, blank = True)

    def __str__(self):
        return self.project

DNA = 'D'
RNA = 'R'
PROTEIN = 'P'
EPIGENETIC = 'E'
OTHER = 'O'
SAMPLE_TYPE_CHOICES = (
    (DNA, 'DNA'),
    (RNA, 'RNA'),
    (PROTEIN, 'Protein'),
    (EPIGENETIC, 'Epigenetic'),
    (OTHER, 'Other'),
)

class Sample(models.Model):
    sample = models.CharField(max_length=200, blank = True)
    type = models.CharField(max_length=1, choices=SAMPLE_TYPE_CHOICES)
    notes = models.TextField
    plant = models.ForeignKey('Plant', on_delete=models.CASCADE, blank = True)
    #do we need accession if we have plant ?
    accession = models.ForeignKey('Accession', on_delete=models.CASCADE, blank = True)

    def __str__(self):
        return self.sample

#sequencing tech
#sequencing center
#sequencing company
#sequencing tracking number
#sra
#pcr free or not
#coverage
#strategy (paired or single) pe-150,se-150, .etc.

class Staff(models.Model):
    staffname = models.CharField(max_length=200, blank = True)

    def __str__(self):
        return self.staffname
