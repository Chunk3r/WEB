#--------------------------------------
# WEB 2019/2020
# Aufgabe P2 / Anwendungsrahmen
#--------------------------------------

import cherrypy

#----------------------------------------------------------
class Abteilung_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self, db_opl, view_opl):
   #-------------------------------------------------------
      self.db_o = db_opl.getStorage_px('abteilung')
      self.defaults_o = db_opl.getDefaults_px('abteilung')
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
   def save(self, id_spl, bezeichnung_spl, beschreibung_spl, mID_o):
   #-------------------------------------------------------
      id_s = id_spl
      data_o = {
         "bezeichnung": bezeichnung_spl,
         "beschreibung": beschreibung_spl,
         "mID": mID_o
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
      return self.view_o.create_px('alist', data_o)

   #-------------------------------------------------------
   def createForm_p(self, id_spl = None):
   #-------------------------------------------------------
      if id_spl != None:
         data_o = self.db_o.read_px(id_spl)
      else:
         data_o = self.defaults_o

      return self.view_o.create_px('aform', data_o, id_spl)

# EOF
