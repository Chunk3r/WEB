#--------------------------------------
# WEB 2019/2020
# Aufgabe P2 / Anwendungsrahmen
#--------------------------------------

import codecs
import os.path

from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions

#----------------------------------------------------------
class View_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self, currDir_spl):
   #-------------------------------------------------------
      templateDir_s = os.path.join(currDir_spl, 'templates')
      self.lookup_o = TemplateLookup(templateDir_s, module_directory=templateDir_s)

      self.templateMethods_o = {
         'elist': [
            'elist.tpl.html',
            self.createList_p,
            False # ohne id
         ],
         'eform': [
            'eform.tpl.html',
            self.createForm_p,
            True # mit id
         ],
         'alist': [
            'alist.tpl.html',
            self.createList_p,
            False # ohne id
         ],
         'aform': [
            'aform.tpl.html',
            self.createForm_p,
            True # mit id
         ]
      }

   #-------------------------------------------------------
   def create_px(self, viewType_spl, data_opl, id_spl = None):
   #-------------------------------------------------------
      markup_s = ''
      if viewType_spl in self.templateMethods_o:
         templateName_s   = self.templateMethods_o[viewType_spl][0]
         templateMethod_o = self.templateMethods_o[viewType_spl][1]
         if self.templateMethods_o[viewType_spl][2]:
            markup_s = templateMethod_o(templateName_s, id_spl, data_opl)
         else:
            markup_s = templateMethod_o(templateName_s, data_opl)
      return markup_s

   #-------------------------------------------------------
   def createList_p(self, templateName_spl, data_opl):
   #-------------------------------------------------------
      try:
         template_o = self.lookup_o.get_template(templateName_spl)
         markup_s = template_o.render(data_o = data_opl)
      except:
         print(exceptions.text_error_template().render())
         markup_s = exceptions.html_error_template().render()
      return markup_s

   #-------------------------------------------------------
   def createForm_p(self, templateName_spl, id_spl, data_opl):
   #-------------------------------------------------------
      try:
         template_o = self.lookup_o.get_template(templateName_spl)
         markup_s = template_o.render(data_o = data_opl, key_s = id_spl)
      except:
         print(exceptions.text_error_template().render())
         markup_s = exceptions.html_error_template().render()
      return markup_s

# EOF
