from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from lims.settings import BASE_DIR
from lims_data_importer.utils import *
from lims.models import Accession, Project, Sample
import os
import datetime
import time
import re

class Command(BaseCommand):
    help = 'Import sample data records'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        with open(os.path.join(BASE_DIR, 'lims_data_importer', 'data', 'lims_data', 'sample_data.csv'), 'r', newline='') as raw_input_file:
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

    def get_accession(self, row):
        return Accession.objects.get(accession=row['Accessions'])

    def get_project(self, row):
        return Project.objects.get(project=row['Project'])

    def make_sample(self, row):
        sample = Sample()
        sample.accession = self.get_accession(row)
        sample.project.add(self.get_project(row))
        sample.sranumber = row['Sranumber']
        sample.strategy = row['Strategy']
        sample.sequenceinstrument = row['Sequenceinstrument']
        sample.sequencingcompany = row['Sequencingcompany']
        sample.tissue_type = row['Tissue type']
        sample.time_point = row['Time point']
        sample.dev_time_point = row['Dev time point']
        sample.file_names = row['filename'] + '\n' + row['filename2']
        sample.file_location = row['File Location']
        return sample

    def handle_row(self, row):
        self.clean_row(row)
        sample = self.make_sample(row)
        sample.save()    
