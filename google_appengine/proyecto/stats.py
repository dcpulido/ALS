from google.appengine.api import users
from google.appengine.ext import ndb

import os
import webapp2
import jinja2
import time

from partida import Partida
from jugador import Jugador
from equipo import Equipo

from equipoEnt import equipoEnt
from partidaEnt import partidaEnt

class statsHandler(webapp2.RequestHandler):
    def get(self):
        try:
            name = self.request.GET['name']
            win = self.request.GET['win']
            lose = self.request.GET['lose']
        except:
            name = None
            win = None
            lose=None

        if name == None:
            self.redirect("/main")
            return
        if win == None:
            self.redirect("/main")
            return
        if lose == None:
            self.redirect("/main")
            return
        else:      
			partida=Partida.query(ndb.AND(Partida.name==name,Partida.user_id==users.get_current_user().user_id()))
			win=Equipo.query(ndb.AND(Equipo.name==win,Equipo.user_id==users.get_current_user().user_id()))
			lose=Equipo.query(ndb.AND(Equipo.name==lose,Equipo.user_id==users.get_current_user().user_id()))


			for ga in partida:
				ga.estado="jugado"
				ga.put()

			for w in win:
				w.wins=w.wins+1
				lo=w.loses
				if w.loses == 0:lo=1
				w.ratio=w.wins/lo
				w.elo=w.elo+10
				w.put()

			for w in lose:
				w.loses=w.loses+1
				w.ratio=w.wins/w.loses
				w.elo=w.elo-10
				w.put()

			time.sleep(1)
			self.redirect("/main")
