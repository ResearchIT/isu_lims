from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from lims.settings import BASE_DIR
from lims_data_importer.utils import *
from lims.models import Accession
import os
import datetime
import time
import re

class Command(BaseCommand):
    help = 'Import accession data records'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        with open(os.path.join(BASE_DIR, 'lims_data_importer', 'data', 'lims_data', 'BYUAccessions.csv'), 'r', newline='') as raw_input_file:
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

    def make_accession(self, row):
        accession = Accession()
        accession.accession = row['Accession']
        accession.species = row['Species']
        accession.genome = row['Genome']
        accession.subgenus = row['Subgenus']
        accession.genus = row['Genus']
        accession.save()
        return accession

    def handle_row(self, row):
        self.clean_row(row)
        accession = self.make_accession(row)
