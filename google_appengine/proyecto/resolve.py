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

class resolveHandler(webapp2.RequestHandler):
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
            partidas=Partida.query(ndb.AND(Partida.user_id==users.get_current_user().user_id(),Partida.name==name))
            for partida in partidas:
                par=partidaEnt(partida.name,partida.nameEquipoA,partida.nameEquipoB,partida.estado,users.get_current_user().user_id())
        template_values = {
            "partida":par
        }

        template = JINJA_ENVIRONMENT.get_template( "game.html" )
        self.response.write(template.render(template_values));