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
        template = JINJA_ENVIRONMENT.get_template( "addGame.html" )
        self.response.write(template.render());
    def get_input(self):
        self.name = self.request.get("name", "")
        self.equipoA = self.request.get("equipoA", 0)
        self.equipoB = self.request.get("equipoB", 0)
        self.estado = self.request.get("estado", "pendiente")
        user = users.get_current_user()
        self.user = user.nickname()
        self.id=int(self.request.get("id",0))

    def post(self):
        self.get_input()
        p1=Partida()
        p1.name=self.name
        p1.idEquipoA=self.equipoA
        p1.idEquipoB=self.equipoB
        p1.user=self.user
        p1.id=self.id
        p1.estado=self.estado
        p1.put()
        self.redirect("/main")

	
