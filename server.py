#--------------------------------------
# WEB 2019/2020
# Aufgabe P2 / Anwendungsrahmen
#--------------------------------------

import sys
import cherrypy

from app import application

#--------------------------------------
def main():
#--------------------------------------
   currDir_s = sys.path[0]
   # disable autoreload
   cherrypy.engine.autoreload.unsubscribe()
   # Static content config
   static_config = {
      '/': {
         'tools.staticdir.root': currDir_s,
         'tools.staticdir.on': True,
         'tools.staticdir.dir': './content'
      }
   }
   # Mount static content handler
   cherrypy.tree.mount(application.Application_cl(currDir_s), '/', static_config)
   # suppress traceback-info
   cherrypy.config.update({'request.show_tracebacks': False})
   # Start server
   cherrypy.engine.start()
   cherrypy.engine.block()

#--------------------------------------
if __name__ == '__main__':
#--------------------------------------
   main()
# EOF