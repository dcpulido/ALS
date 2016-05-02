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

class teamAddHandler(webapp2.RequestHandler):
    def get(self):
        pla=Jugador.query(Jugador.user_id==users.get_current_user().user_id())
        equ=Equipo.query(Equipo.user_id==users.get_current_user().user_id())
        players=[]
        equipos=[]
        for p in pla:players.append(p)
        for p in equ:equipos.append(p)
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
        if p1.name == "":self.redirect("/addTeam")
        p1.nameJug1=self.namet1
        p1.nameJug2=self.namet2 
        p1.ratio=0
        p1.elo=1000
        p1.wins=0
        p1.loses=0
        p1.user_id=users.get_current_user().user_id()
        if Equipo.query(ndb.AND(Equipo.name==p1.name,Equipo.user_id==users.get_current_user().user_id())).count()==0:
            p1.put()
            time.sleep(1)
            self.redirect("/addTeam")
        else:
            self.redirect("/addTeam")


      
	
