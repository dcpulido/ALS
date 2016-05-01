from google.appengine.ext import ndb

class Jugador(ndb.Model):
	posicion = ndb.StringProperty(required = True)
	name = ndb.StringProperty(required = True)
