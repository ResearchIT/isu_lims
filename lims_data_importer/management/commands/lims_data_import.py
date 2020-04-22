from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from lims.settings import BASE_DIR
from lims_data_importer.utils import *
from lims.models import Accession, SeedPacket
import os
import datetime
import time
import re

class Command(BaseCommand):
    help = 'Import lims records'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        with open(os.path.join(BASE_DIR, 'lims_data_importer', 'data', 'lims_data', 'seed_count.csv'), 'r', newline='') as raw_input_file:
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

    def make_seed_packet(self, row):
        packet = SeedPacket()
        packet.accession = get_accession(row)
        packet.notes = row['Notes']
        if row['Parent A'] != "":
            packet.parenta = int(row['Parent A'])
        packet.quantity = int(row['Quantity'])
        packet.location = row['Location']
        if row['Date collected'] != "" and row['Date collected'] != "NA":
            packet.datecollected = datetime.date(*(time.strptime(row['Date collected'] + " 00:00 -0500", "%m/%d/%Y %H:%M %z")[0:3]))
        return packet

    def handle_row(self, row):
        self.clean_row(row)
        packet = self.make_seed_packet(row)
        packet.save()    
