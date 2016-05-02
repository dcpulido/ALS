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

class MainMenuHandler(webapp2.RequestHandler):
	def get(self):
		def montaEquipos(self):
			toret=[]
			for equipo in Equipo.query(Equipo.user_id==users.get_current_user().user_id()):
				toret.append(equipoEnt(equipo.name,equipo.nameJug1,equipo.nameJug2,users.get_current_user().user_id()))
			return toret

		def montaPartidas(self):
			toret=[]
			for partida in Partida.query(Partida.user_id==users.get_current_user().user_id()):
				toret.append(partidaEnt(partida.name,partida.nameEquipoA,partida.nameEquipoB,partida.estado,users.get_current_user().user_id()))
			return toret

		user = users.get_current_user()


		user_name = user.email()
		print("llegoaki")
		access_link = users.create_logout_url("/")
		juga = Jugador.query(Jugador.user_id==users.get_current_user().user_id())
		jugadores=[]
		for j in juga: jugadores.append(j)
		equipos = montaEquipos(self)
		partidas = montaPartidas(self)
		template_values = {
			"user_name": user_name,
			"access_link": access_link,
			"partidas":partidas,
			"jugadores":jugadores,
			"equipos":equipos
		}

		template = JINJA_ENVIRONMENT.get_template( "mainMenu.html" )
		self.response.write(template.render(template_values));
		

		