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

class playerAddHandler(webapp2.RequestHandler):
    def get(self):
        players=Jugador.query()
        template_values = {
                "jugadores":players
            }
        template = JINJA_ENVIRONMENT.get_template( "addPlayer.html" )
        self.response.write(template.render(template_values));
    def get_input(self):
        self.name = self.request.get("name", "")
        self.id = int(self.request.get("id", 0))
        self.posicion = self.request.get("posicion", 0)
       

    def post(self):
        self.get_input()
        p1=Jugador()
        p1.name=self.name
        p1.posicion=self.posicion
        p1.id=self.id
        players=Jugador.query()
        flag=True
        for jugador in players:
            if jugador.id==self.id:
                flag=False
        if flag==True:
            p1.put()
            self.redirect("/main")
        else:
            self.redirect("/main")

	
