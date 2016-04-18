

class Jugador():
	#user = ndb.StringProperty(required = True)
	#name = ndb.StringProperty(required = True)
	def __init__(self,id,na):
		self.__id=id
		self.__name=na

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		self.__name=value

	@property
	def id(self):
		return self.__id

	@id.setter
	def id(self, value):
		self.__id=value
