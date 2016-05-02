from google.appengine.ext import ndb

class Equipo(ndb.Model):
	name = ndb.StringProperty(required = True)
	nameJug1=ndb.StringProperty(required = True)
	nameJug2=ndb.StringProperty(required = True)
	user_id = ndb.StringProperty(required = True)
	ratio = ndb.FloatProperty()
	elo = ndb.FloatProperty()
	wins = ndb.IntegerProperty()
	loses = ndb.IntegerProperty()
