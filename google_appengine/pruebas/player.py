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

class playerHandler(webapp2.RequestHandler):
    def get(self):
        try:
    	    name = self.request.GET['name']
            print(str.format("esto es el atrib {0}",name))
        except:
            name = None

        if name == None:
            self.redirect("/player")
            return
        else:      
            jugadores=Jugador.query()
            for jugador in jugadores:
                if jugador.name==name:
                    toret =jugador
            
        template_values = {
            "name":toret.name
        }

        template = JINJA_ENVIRONMENT.get_template( "player.html" )
        self.response.write(template.render(template_values));