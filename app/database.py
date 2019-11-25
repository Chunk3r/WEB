#--------------------------------------
# WEB 2019/2020
# Aufgabe P2 / Anwendungsrahmen
#--------------------------------------

import os
import os.path
import codecs
import json

from . import dataid
from . import storage

#----------------------------------------------------------
class Database_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self, currDir_spl):
   #-------------------------------------------------------
      self.maxId_o = dataid.DataId_cl(currDir_spl)
      self.types_o = {
         'employee': {
            'storage': storage.Storage_cl('employee', currDir_spl, self.maxId_o),
            'defaults': {
               "name": "",
               "vorname": "",
               "funktion": "Mitarbeiter",
               "urlaubstage": 28
            }
         }
      }

   #-------------------------------------------------------
   def getStorage_px(self, type_spl):
   #-------------------------------------------------------
      storage_o = None
      if type_spl in self.types_o:
         storage_o = self.types_o[type_spl]['storage']
      return storage_o

   #-------------------------------------------------------
   def getDefaults_px(self, type_spl):
   #-------------------------------------------------------
      defaults_o = None
      if type_spl in self.types_o:
         defaults_o = self.types_o[type_spl]['defaults']
      return defaults_o

# EOF