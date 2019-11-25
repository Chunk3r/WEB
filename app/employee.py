#--------------------------------------
# WEB 2019/2020
# Aufgabe P2 / Anwendungsrahmen
#--------------------------------------

import cherrypy

#----------------------------------------------------------
class Employee_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self, db_opl, view_opl):
   #-------------------------------------------------------
      self.db_o = db_opl.getStorage_px('employee')
      self.defaults_o = db_opl.getDefaults_px('employee')
      self.view_o = view_opl

   @cherrypy.expose
   #-------------------------------------------------------
   def index(self):
   #-------------------------------------------------------
      return self.createList_p()

   @cherrypy.expose
   #-------------------------------------------------------
   def add(self):
   #-------------------------------------------------------
      return self.createForm_p()

   @cherrypy.expose
   #-------------------------------------------------------
   def edit(self, id_spl):
   #-------------------------------------------------------
      return self.createForm_p(id_spl)

   @cherrypy.expose
   #-------------------------------------------------------
   def save(self, id_spl, name_spl, vorname_spl, funktion_spl, urlaubstage_ipl):
   #-------------------------------------------------------
      id_s = id_spl
      data_o = {
         "name": name_spl,
         "vorname": vorname_spl,
         "funktion": funktion_spl,
         "urlaubstage": int(urlaubstage_ipl)
      }
      if id_s != "None":
         self.db_o.update_px(id_s, data_o)
      else:
         id_s = self.db_o.create_px(data_o)

      return self.createForm_p(id_s)

   @cherrypy.expose
   #-------------------------------------------------------
   def delete(self, id_spl):
   #-------------------------------------------------------
      self.db_o.delete_px(id_spl)
      return self.createList_p()

   #-------------------------------------------------------
   def createList_p(self):
   #-------------------------------------------------------
      data_o = self.db_o.read_px()
      # bessere Lösung erstellen!
      for key_s in data_o:
         data_o[key_s]["urlaubist"] = 0
      return self.view_o.create_px('elist', data_o)

   #-------------------------------------------------------
   def createForm_p(self, id_spl = None):
   #-------------------------------------------------------
      if id_spl != None:
         data_o = self.db_o.read_px(id_spl)
      else:
         data_o = self.defaults_o
      # ERGÄNZEN: Urlaubstage min/max etc.
      data_o["minurlaub"] = 24
      data_o["maxurlaub"] = 30
      return self.view_o.create_px('eform', data_o, id_spl)

# EOF