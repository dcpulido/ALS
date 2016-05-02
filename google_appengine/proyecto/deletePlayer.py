from google.appengine.api import users
from google.appengine.ext import ndb

import time
import os
import webapp2
import jinja2

from partida import Partida
from jugador import Jugador
from equipo import Equipo

class playerDeleteHandler(webapp2.RequestHandler):
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
            jugador=Jugador.query(Jugador.name==name)
            teams=Equipo.query(ndb.OR(Equipo.nameJug1==name,Equipo.nameJug2==name))
            names=[]
            for eq in teams:
                names.append(eq.name)
                eq.key.delete()

            games=Partida.query()
            for ga in games:
                for name in names:
                    if ga.nameEquipoA== name:
                        ga.key.delete()
                    if ga.nameEquipoB== name:
                        ga.key.delete()
            for jug in jugador:
                jug.key.delete()
            time.sleep(1)
            self.redirect("/main")
   

	
