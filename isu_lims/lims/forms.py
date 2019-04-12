from django.forms import ModelForm
from django import forms
from .models import SeedPacket

class NewSeedPacketForm(ModelForm):
    class Meta:
        model = SeedPacket
        fields = ['notes', 'parenta', 'parentb', 'quantity', 'datecollected', 'accession']
