from google.appengine.ext import ndb

class Equipo(ndb.Model):
	id=ndb.IntegerProperty(required = True)
	name = ndb.StringProperty(required = True)
	idJug1=ndb.IntegerProperty()
	idJug2=ndb.IntegerProperty()
