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

class teamAddHandler(webapp2.RequestHandler):
    def get(self):
        players=Jugador.query()
        equipos=Equipo.query()
        template_values = {
                "jugadores":players,
                "equipos":equipos
            }
        template = JINJA_ENVIRONMENT.get_template( "addTeam.html" )
        self.response.write(template.render(template_values));
    def get_input(self):
        self.name = self.request.get("name", "")
        self.namet1 = self.request.get("nameJug1", "")
        self.namet2 = self.request.get("nameJug2", "")
        
        
       

    def post(self):
        self.get_input()
        p1=Equipo()
        p1.name=self.name
        p1.nameJug1=self.namet1
        p1.nameJug2=self.namet2
        p1.put()
        self.redirect("/main")

	
