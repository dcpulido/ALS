from google.appengine.api import users
from google.appengine.ext import ndb
import os
import webapp2
import jinja2

from equipo import Equipo
from jugador import Jugador
from partida import Partida
from equipoEnt import equipoEnt
from partidaEnt import partidaEnt

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ["jinja2.ext.autoescape"],
    autoescape = True)

class indexHandler(webapp2.RequestHandler):
    def get(self):


		user_name = "Logout"
		user = users.get_current_user()
		access_link = users.create_logout_url("/")
		if user == None:
			self.redirect("/")
		toret=[]
		for partida in Partida.query(ndb.AND(Partida.user_id==users.get_current_user().user_id(),Partida.estado=="pendiente")):
			toret.append(partidaEnt(partida.name,partida.nameEquipoA,partida.nameEquipoB,partida.estado,users.get_current_user().user_id()))

		template_values = {
		    "user_name": user_name,
		    "access_link": access_link,
		    "partidas":toret
		}

		template = JINJA_ENVIRONMENT.get_template( "index.html" )
		self.response.write(template.render(template_values))
