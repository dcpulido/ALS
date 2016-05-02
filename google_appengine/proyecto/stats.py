from google.appengine.api import users
from google.appengine.ext import ndb

import os
import webapp2
import jinja2

from partida import Partida
from jugador import Jugador
from equipo import Equipo

from equipoEnt import equipoEnt
from partidaEnt import partidaEnt

class statsHandler(webapp2.RequestHandler):
    def get(self):
        try:
            name = self.request.GET['name']
            win = self.request.GET['win']
            lose = self.request.GET['lose']
        except:
            name = None
            win = None
            lose=None

        if name == None:
            self.redirect("/main")
            return
        if win == None:
            self.redirect("/main")
            return
        if lose == None:
            self.redirect("/main")
            return
        else:      
            partida=Partida.query(ndb.AND(Partida.name==name,Partida.user_id==users.get_current_user().user_id()))
            win=Jugador.query(ndb.AND(Jugador.name==win,Jugador.user_id==users.get_current_user().user_id()))
            games=Partida.query(ndb.AND(ndb.OR(Partida.nameJugadorA==name,Partida.nameEquipoB==name),Partida.user_id==users.get_current_user().user_id()))
            names=[]
            for ga in games:
                names.append(ga.name)
                ga.key.delete()

            for jug in equipo:
                jug.key.delete()
            time.sleep(1)
            self.redirect("/main")
