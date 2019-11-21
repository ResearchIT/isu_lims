import csv
import datetime
import time

class FileWrapper(object):
  def __init__(self, f):
    self.f = f
    self.last_line = None

  def __iter__(self):
    return self

  def __next__(self):
    self.last_line = next(self.f)
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