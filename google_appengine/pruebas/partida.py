from google.appengine.ext import ndb

class Partida(ndb.Model):
	id=ndb.IntegerProperty(required = True)
	user = ndb.StringProperty(required = True)
	name = ndb.StringProperty(required = True)
	idEquipoA = ndb.IntegerProperty()
	idEquipoB = ndb.IntegerProperty()
	estado= ndb.StringProperty(required = True)