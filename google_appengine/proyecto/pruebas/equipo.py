from google.appengine.ext import ndb

class Equipo(ndb.Model):
	name = ndb.StringProperty(required = True)
	idJug1=ndb.IntegerProperty()
	ifJug2=ndb.IntegerProperty()
