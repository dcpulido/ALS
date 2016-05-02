from google.appengine.api import users
from google.appengine.ext import ndb

import time
import os
import webapp2
import jinja2

from partida import Partida
from jugador import Jugador
from equipo import Equipo

class gameDeleteHandler(webapp2.RequestHandler):
    def get(self):
        try:
            name = self.request.GET['name']
            print(str.format("esto es el atrib {0}",name))
        except:
            name = None

        if name == None:
            self.redirect("/main")
            return
        else:      
            partida=Partida.query(ndb.AND(Partida.name==name,Partida.user_id==users.get_current_user().user_id()))
            for pa in partida:
                pa.key.delete()
            time.sleep(1)
            self.redirect("/main")
   