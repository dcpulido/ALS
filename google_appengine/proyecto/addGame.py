from google.appengine.api import users
from google.appengine.ext import ndb


import os
import webapp2
import jinja2

from partida import Partida
from jugador import Jugador
from equipo import Equipo

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ["jinja2.ext.autoescape"],
    autoescape = True)

class gameAddHandler(webapp2.RequestHandler):
    def get(self):
        equipos=Equipo.query()
        template_values = {
                "equipos":equipos
        }
        template = JINJA_ENVIRONMENT.get_template( "addGame.html" )
        self.response.write(template.render(template_values));
    def get_input(self):
        self.name = self.request.get("name", "")
        self.equipoA = self.request.get("equipoA", "")
        self.equipoB = self.request.get("equipoB", "")
        self.estado = self.request.get("estado", "pendiente")

    def post(self):
        self.get_input()
        p1=Partida()
        p1.name=self.name
        p1.nameEquipoA=self.equipoA
        p1.nameEquipoB=self.equipoB
        p1.estado=self.estado
        p1.put()
        self.redirect("/main")

	
