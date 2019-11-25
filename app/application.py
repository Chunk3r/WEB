#--------------------------------------
# WEB 2019/2020
# Aufgabe P2 / Anwendungsrahmen
#--------------------------------------

import cherrypy

from . import database
from . import view
from . import employee
from . import abteilung

#----------------------------------------------------------
class Application_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self, currDir_spl):
   #-------------------------------------------------------
      self.db_o = database.Database_cl(currDir_spl)
      self.view_o = view.View_cl(currDir_spl)
      self.employee = employee.Employee_cl(self.db_o, self.view_o)

   @cherrypy.expose
   #-------------------------------------------------------
   def index(self):
   #-------------------------------------------------------
      return self.createIndex_p()

   @cherrypy.expose
   #-------------------------------------------------------
   def default(self, *arguments, **kwargs):
   #-------------------------------------------------------
      msg_s = "unbekannte Anforderung: " + \
      str(arguments) + \
      ' ' + \
      str(kwargs)
      raise cherrypy.HTTPError(404, msg_s)

   #-------------------------------------------------------
   def createIndex_p(self):
   #-------------------------------------------------------
      data_o = None
      return self.view_o.create_px('index', data_o)
# EOF
