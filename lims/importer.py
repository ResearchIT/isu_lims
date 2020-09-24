import csv
import datetime
import time
import glob
import os
import io
import zipfile
from lims.settings import BASE_DIR

REJECTS_DIR = [BASE_DIR, 'lims_data_importer', 'data', 'lims_data', 'rejects']

class FileWrapper(object):
  def __init__(self, f):
    self.f = iter(f)
    self.last_line = None

  def __iter__(self):
    return self

  def __next__(self):
    self.last_line = next(self.f).decode('UTF-8')
    return self.last_line

class LimsCSVReader(csv.DictReader):

    @property                                    
    def fieldnames(self):
        if self._fieldnames is None:
            csv.DictReader.fieldnames.__get__(self)
            if self._fieldnames is not None:
                self._fieldnames = [name.strip() for name in self._fieldnames]
        return self._fieldnames

class LimsDataEntryException(Exception):
    pass

def empty_rejects_directory():
    existing_rejects_file_list = glob.glob(os.path.join(*REJECTS_DIR, '*.txt'))
    for reject_file in existing_rejects_file_list:
        os.remove(reject_file)

def get_reject_filepath(proposed_filename):
    cleaned_filename = "".join([c for c in proposed_filename if c.isalpha() or c.isdigit() or c==' ']).rstrip()
    return os.path.join(*REJECTS_DIR, cleaned_filename + '.txt')

def zip_rejects():
    zip_buf = io.BytesIO()
    zipf = zipfile.ZipFile(zip_buf, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(os.path.join(*REJECTS_DIR)):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.basename(file))
    zipf.close()
    return zip_buf.getvalue()