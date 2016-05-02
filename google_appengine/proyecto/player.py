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
            jugadores=Jugador.query(Jugador.user_id==users.get_current_user().user_id())
            partidas=Partida.query(Partida.user_id==users.get_current_user().user_id())
            equipos=Equipo.query(Equipo.user_id==users.get_current_user().user_id())
            

            for jugador in jugadores:
                if jugador.name==name:
                    toret =jugador


            eq=[]
            for equipo in equipos:
                if equipo.nameJug1==name  :
                    flag=True
                    for e in eq:
                        if e.name==equipo.name:flag=False
                    if flag==True:eq.append(equipoEnt(equipo.name,equipo.nameJug1,equipo.nameJug2,users.get_current_user().user_id())) 
                if equipo.nameJug2==name :
                    flag=True
                    for e in eq:
                        if e.name==equipo.name:flag=False
                    if flag==True:eq.append(equipoEnt(equipo.name,equipo.nameJug1,equipo.nameJug2,users.get_current_user().user_id()))
                    

            ga=[]
            for partida in partidas:
                for e in eq:
                    if partida.nameEquipoA==e.name :
                        flag=True
                        for g in ga:
                            if g.name==partida.name:flag=False
                        if flag==True:ga.append(partidaEnt(partida.name,partida.nameEquipoA,partida.nameEquipoB,partida.estado,users.get_current_user().user_id())) 
                    if partida.nameEquipoB==e.name :
                        flag=True
                        for g in ga:
                            if g.name==partida.name:flag=False
                        if flag==True:ga.append(partidaEnt(partida.name,partida.nameEquipoA,partida.nameEquipoB,partida.estado,users.get_current_user().user_id())) 

        template_values = {
            "name":toret.name,
            "posicion":toret.posicion,
            "equipos":eq,
            "partidas":ga
        }

        template = JINJA_ENVIRONMENT.get_template( "player.html" )
        self.response.write(template.render(template_values));