from django import forms
from .models import SeedPacket

class NewSeedPacketForm(forms.ModelForm):
    class Meta:
        model = SeedPacket
        fields = ['notes', 'parenta', 'parentb', 'quantity', 'datecollected', 'accession']
