from google.appengine.ext import ndb

class Partida(ndb.Model):
	name = ndb.StringProperty(required = True)
	nameEquipoA = ndb.StringProperty(required = True)
	nameEquipoB = ndb.StringProperty(required = True)
	estado= ndb.StringProperty(required = True)
	user_id = ndb.StringProperty(required = True)