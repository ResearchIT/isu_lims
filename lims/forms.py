from django import forms
from django.db import transaction
from lims.settings import BASE_DIR
from lims.importer import *
from lims.models import Accession, Project, Sample, SeedPacket
import os
import datetime
import time
import re

class SampleImportForm(forms.Form):

    csv_file = forms.FileField()

    def import_from_csv(self, raw_input_file):

        empty_rejects_directory()

        input_file = FileWrapper(raw_input_file)
        reader = LimsCSVReader(input_file, delimiter=",", quotechar="\"")
        row_number = 0
        for row in reader:
            try:
                with transaction.atomic():
                    self.handle_row(row)
            except Exception as e:
                with open(get_reject_filepath(str(e)), 'a') as rejects_file:
                    rejects_file.write(input_file.last_line)
        
        return zip_rejects()

    def clean_row(self, row):

        for key in row:
            row[key] = row[key].strip()

    def get_accession(self, row):
        return Accession.objects.get(accession=row['accession'])

    def get_project(self, row):
        return Project.objects.get(project=row['project'])

    def make_sample(self, row):
        sample = Sample()
        sample.accession = self.get_accession(row)
        sample.sample = row['sample']
        sample.sranumber = row['sranumber']
        sample.strategy = row['strategy']
        sample.sequenceinstrument = row['sequenceinstrument']
        sample.sequencingcompany = row['sequencingcompany']
        sample.tissue_type = row['tissue_type']
        sample.time_point = row['time_point']
        sample.dev_time_point = row['dev_time_point']
        sample.file_names = row['file_names']
        sample.file_location = row['file_location']
        sample.notes = row['notes']
        sample.trackingnumber = row['trackingnumber']
        sample.coverage = row['coverage']
        sample.pcrfree = row['pcrfree'] == "YES"
        sample.category = Sample.ESampleType[row['category']]
        sample.save()
        sample.project.add(self.get_project(row))
        return sample

    def handle_row(self, row):
        self.clean_row(row)
        sample = self.make_sample(row)
        sample.save()

class SeedpacketImportForm(forms.Form):

    csv_file = forms.FileField()

    def import_from_csv(self, raw_input_file):

        empty_rejects_directory()

        input_file = FileWrapper(raw_input_file)
        reader = LimsCSVReader(input_file, delimiter=",", quotechar="\"")
        row_number = 0
        for row in reader:
            try:
                with transaction.atomic():
                    self.handle_row(row)
            except Exception as e:
                with open(get_reject_filepath(str(e)), 'a') as rejects_file:
                    rejects_file.write(input_file.last_line)
        
        return zip_rejects()

    def clean_row(self, row):
        for key in row:
            row[key] = row[key].strip()

    def get_accession(self, row):
        return Accession.objects.get(accession=row['accession'])

    def make_seed_packet(self, row):
        packet = SeedPacket()
        packet.accession = self.get_accession(row)
        packet.notes = row['notes']
        packet.quantity = int(row['quantity'])
        packet.location = row['location']
        if row['date_collected'] != "" and row['date_collected'] != "NA":
            packet.datecollected = datetime.date(*(time.strptime(row['date_collected'] + " 00:00 -0500", "%m/%d/%Y %H:%M %z")[0:3]))
        if row['parenta'] != "" and row['parenta'] != "NA":
            packet.parenta_id = int(row['parenta'])
        if row['parentb'] != "" and row['parentb'] != "NA":
            packet.parentb_id = int(row['parentb'])
        return packet

    def handle_row(self, row):
        self.clean_row(row)
        packet = self.make_seed_packet(row)
        packet.save()
