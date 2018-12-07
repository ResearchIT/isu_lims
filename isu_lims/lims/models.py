from django.db import models
#I need to practice
class Genus(models.Model):
    genus = models.CharField(max_length=200)

    def __str__(self):
        return self.genus

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
LANDRACE = 'L'
UNKNOWN = 'U'
ACCESSION_TYPE_CHOICES = (
    (WILD, 'Wild'),
    (DOMESTICATED, 'Domesticated'),
    (LANDRACE, 'Landrace'),
    (UNKNOWN, 'Unknown'),
)
class Accession(models.Model):
    accession = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=ACCESSION_TYPE_CHOICES)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)

class Plant(models.Model):
    notes = models.TextField
    fromseed = models.ForeignKey('Seed', on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    offspring = models.ForeignKey('Seed', on_delete=models.CASCADE)
    dateplanted = models.DateField
    samples = models.ForeignKey('Plants', on_delete=models.CASCADE)
    photo = models.ImageField

    #We would also like to include barcode here somehow

class SeedPacket(models.Model):
    notes = models.TextField
    parenta = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='offspringa')
    parentb = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='offspringb')
    quantity = models.IntegerField
    datecollected = models.DateField
    accession = models.ForeignKey(Accession, on_delete=models.CASCADE)

class Seed(models.Model):
    notes = models.TextField
    seed_packet = models.ForeignKey(SeedPacket, on_delete=models.CASCADE)

class Project(models.Model):
    name = models.CharField(max_length=200)
    startdate = models.DateField
    enddate = models.DateField
    url = models.URLField
    grant = models.TextField
    lead = models.CharField(max_length=100)
    projecturl = models.URLField(max_length=300)

DNA = 'D'
RNA = 'R'
Protein = 'P'
Epigenetic = 'E'
Other = 'O'
SAMPLE_TYPE_CHOICES = (
    (DNA, 'DNA'),
    (RNA, 'RNA'),
    (PROTEIN, 'Protein'),
    (EPIGENETIC, 'Epigenetic'),
    (OTHER, 'Other'),
)

class Sample(models.Model):
    type = models.CharField(max_length=1, choices=SAMPLE_TYPE_CHOICES)
    notes = models.TextField
    plant = models.ForeignKey('Plant', on_delete=models.CASCADE)
    accession = models.ForeignKey('Accession', on_delete=models.CASCADE)
