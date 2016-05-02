from google.appengine.ext import ndb

class Jugador(ndb.Model):
	posicion = ndb.StringProperty(required = True)
	name = ndb.StringProperty(required = True)
	user_id = ndb.StringProperty(required = True)
	ratio = ndb.FloatProperty()
	elo = ndb.FloatProperty()
	wins = ndb.IntegerProperty()
	loses = ndb.IntegerProperty()
