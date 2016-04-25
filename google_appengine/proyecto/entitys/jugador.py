from google.appengine.ext import ndb

class Jugador(ndb.Model):
	id=ndb.IntegerProperty(required = True)
	posicion = ndb.StringProperty(required = True)
	name = ndb.StringProperty(required = True)
