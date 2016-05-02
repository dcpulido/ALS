from google.appengine.api import users
from google.appengine.ext import ndb

import time
import os
import webapp2
import jinja2

from partida import Partida
from jugador import Jugador
from equipo import Equipo

class teamDeleteHandler(webapp2.RequestHandler):
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
            equipo=Equipo.query(Equipo.name==name)
            games=Partida.query(ndb.OR(Partida.nameEquipoA==name,Partida.nameEquipoB==name))
            names=[]
            for ga in games:
                names.append(ga.name)
                ga.key.delete()

            for jug in equipo:
                jug.key.delete()
            time.sleep(1)
            self.redirect("/main")
   