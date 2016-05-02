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
JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ["jinja2.ext.autoescape"],
    autoescape = True)

class gameHandler(webapp2.RequestHandler):
    def get(self):
        try:
    	    name = self.request.GET['name']
            print(str.format("esto es el atrib {0}",name))
        except:
            name = None

        if name == None:
            self.redirect("/game")
            return
        else:      
            partidas=Partida.query(Partida.user_id==users.get_current_user().user_id())
            for partida in partidas:
                if partida.name==name:
                    toret =partida
            equipos=Equipo.query(Equipo.user_id==users.get_current_user().user_id())
            for equipo in equipos:
                if equipo.id==toret.idEquipoA:
                    e1 =equipo
            for equipo in equipos:
                if equipo.id==toret.idEquipoB:
                    e2 =equipo
            jugadores=Jugador.query(Jugador.user_id==users.get_current_user().user_id())
            for jugador in jugadores:
                if jugador.id==e1.idJug1:
                    j1 =jugador
            for jugador in jugadores:
                if jugador.id==e1.idJug2:
                    j2 =jugador
            for jugador in jugadores:
                if jugador.id==e2.idJug1:
                    j3 =jugador
            for jugador in jugadores:
                if jugador.id==e2.idJug2:
                    j4 =jugador
        template_values = {
            "partida":toret,
            "e1":e1,
            "e2":e2,
            "j1":j1,
            "j2":j2,
            "j3":j3,
            "j4":j4
        }

        template = JINJA_ENVIRONMENT.get_template( "game.html" )
        self.response.write(template.render(template_values));