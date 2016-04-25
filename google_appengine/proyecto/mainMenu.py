from google.appengine.api import users
from google.appengine.ext import ndb


import os
import webapp2
import jinja2

from partida import Partida
from jugador import Jugador
JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ["jinja2.ext.autoescape"],
    autoescape = True)

class MainMenuHandler(webapp2.RequestHandler):
    def get(self):
		user = users.get_current_user()

		if user != None:
			user_name = user.email()
			access_link = users.create_logout_url("/")
			partidas = Partida.query()
			jugadores = Jugador.query()
			template_values = {
				"user_name": user_name,
				"access_link": access_link,
				"partidas":partidas,
				"jugadores":jugadores
			}

			template = JINJA_ENVIRONMENT.get_template( "mainMenu.html" )
			self.response.write(template.render(template_values));
		else:
			self.redirect("/")