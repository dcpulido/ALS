from google.appengine.ext import ndb

class usuarioReg(ndb.Model):
	email = ndb.StringProperty(required = True)
