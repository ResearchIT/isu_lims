from django.forms import ModelForm
from django import forms
from .models import Genus
from .models import SeedPacket
from .models import Subgenus
from .models import Species
from .models import Accession
from .models import Seed
from .models import Project
from .models import Sample
from .models import Plant
from .models import Genome

class NewSeedPacketForm(ModelForm):
    class Meta:
        model = SeedPacket
        fields = ['notes', 'parenta', 'parentb', 'quantity', 'datecollected', 'accession']

class NewGenusForm(ModelForm):
    class Meta:
        model = Genus
        fields = ['genus']

class NewSubgenusForm(ModelForm):
    class Meta:
        model = Subgenus
        fields = ['subgenus', 'genus']

class NewGenomeForm(ModelForm):
    class Meta:
        model = Genome
        fields = ['genome', 'subgenus']

class NewSpeciesForm(ModelForm):
    class Meta:
        model = Species
        fields = ['species', 'genome']

class NewAccessionForm(ModelForm):
    class Meta:
        model = Accession
        fields = ['accession', 'status', 'species']

class NewPlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = ['notes', 'fromseed', 'location', 'accession', 'flowering', 'sample', 'project']

class NewSeedForm(ModelForm):
    class Meta:
        model = Seed
        fields = ['notes']

class NewProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['project', 'startdate', 'enddate', 'url', 'grantnumber', 'grantagency', 'lead']

class NewSampleForm(ModelForm):
    class Meta:
        model = Sample
        fields = ['sample', 'category', 'notes', 'accession', 'sequencingcompany', 'pcrfree', 'sranumber', 'coverage', 'strategy', 'trackingnumber', 'sequenceinstrument']
