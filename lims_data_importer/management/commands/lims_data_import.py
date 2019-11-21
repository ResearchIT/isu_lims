from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from lims.settings import BASE_DIR
from lims_data_importer.utils import *
from lims.models import Accession, Species, Genome, Subgenus, Genus
import os
import datetime
import re

class Command(BaseCommand):
    help = 'Import lims records'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        with open(os.path.join(BASE_DIR, 'lims_data_importer', 'data', 'lims_data', 'gossypium.csv'), 'r', newline='') as raw_input_file:
            input_file = FileWrapper(raw_input_file)
            reader = LimsCSVReader(input_file, delimiter=",", quotechar="\"")
            row_number = 0
            for row in reader:
                try:
                    with transaction.atomic():
                        self.handle_row(row)
                except Exception as e:
                    proposed_filename = str(e)
                    cleaned_filename = "".join([c for c in proposed_filename if c.isalpha() or c.isdigit() or c==' ']).rstrip()
                    with open(os.path.join(BASE_DIR, 'lims_data_importer', 'data', 'lims_data', 'rejects', cleaned_filename + '.txt'), 'a') as rejects_file:
                        rejects_file.write(input_file.last_line)
                
                if row_number % 20 == 0:
                    self.stdout.write(self.style.SUCCESS('Processed row {}'.format(row_number)))

                row_number += 1

    def clean_row(self, row):

        for key in row:
            row[key] = row[key].strip()

    def get_or_make_species(self, row):
        try:
            existing_species = Species.objects.get(species=row['Species'])
            if existing_species.genome.genome != row['Genome']:
                raise LimsDataEntryException("Found matching species, genome differed")
            species = existing_species
        except Species.DoesNotExist:
            species = Species()
            species.species = row['Species']
            species.genome = self.get_or_make_genome(row)
            species.save()
        return species

    def get_or_make_genome(self, row):
        try:
            existing_genome = Genome.objects.get(genome=row['Genome'])
            if existing_genome.subgenus.subgenus != row['Subgenus']:
                raise LimsDataEntryException("Found matching genome, subgenus differed")
            genome = existing_genome
        except Genome.DoesNotExist:
            genome = Genome()
            genome.genome = row['Genome']
            genome.subgenus = self.get_or_make_subgenus(row)
            genome.save()
        return genome

    def get_or_make_subgenus(self, row):
        try:
            existing_subgenus = Subgenus.objects.get(subgenus=row['Subgenus'])
            if existing_subgenus.genus.genus != row['Genus']:
                raise LimsDataEntryException("Found matching subgenus, genus differed")
            subgenus = existing_subgenus
        except Subgenus.DoesNotExist:
            subgenus = Subgenus()
            subgenus.subgenus = row['Subgenus']
            subgenus.genus = self.get_or_make_genus(row)
            subgenus.save()
        return subgenus

    def get_or_make_genus(self, row):
        try:
            existing_genus = Genus.objects.get(genus=row['Genus'])
            genus = existing_genus
        except Genus.DoesNotExist:
            genus = Genus()
            genus.genus = row['Genus']
            genus.save()
        return genus

    def make_accession(self, row):
        accession = Accession()
        accession.species = self.get_or_make_species(row)
        accession.accession = row['Plant Name']
        accession.pinumber = row['Plant ID']
        accession.alternatenames = row['Other names']
        return accession

    def handle_row(self, row):
        self.clean_row(row)
        accession = self.make_accession(row)
        accession.save()    
