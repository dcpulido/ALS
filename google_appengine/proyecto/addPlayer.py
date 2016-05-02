from google.appengine.api import users
from google.appengine.ext import ndb

import time
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
        pla=Jugador.query(Jugador.user_id==users.get_current_user().user_id())
        players=[]
        for p in pla:players.append(p)
        template_values = {
                "jugadores":players
            }
        template = JINJA_ENVIRONMENT.get_template( "addPlayer.html" )
        self.response.write(template.render(template_values));
    def get_input(self):
        self.name = self.request.get("name", "")
        self.posicion = self.request.get("posicion", 0)
       

    def post(self):
        self.get_input()
        p1=Jugador()
        p1.name=self.name
        if p1.name == "":self.redirect("/addPlayer")
        p1.posicion=self.posicion
        p1.user_id=users.get_current_user().user_id()
        p1.ratio=0
        p1.elo=1000
        p1.wins=0
        p1.loses=0
        pla=Jugador.query(Jugador.user_id==users.get_current_user().user_id())
        players=[]
        for p in pla:players.append(p)
        flag=True
        for jugador in players:
            if jugador.name==self.name:
                flag=False
        if flag==True:
            p1.put()
            time.sleep(1)
            self.redirect("/addPlayer")
        else:
            self.redirect("/addPlayer")

	
