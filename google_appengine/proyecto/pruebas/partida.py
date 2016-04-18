

class Partida():
	#user = ndb.StringProperty(required = True)
	#name = ndb.StringProperty(required = True)
	def __init__(self,us,na):
		self.__user=us
		self.__name=na
		self.__jugadores=[]

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		self.__name=value

	@property
	def user(self):
		return self.__user

	@user.setter
	def user(self, value):
		self.__user=value

	@property
	def jugadores(self):
		return self.__jugadores

	@jugadores.setter
	def jugadores(self, value):
		self.__jugadores=value

	def addJugador(self, value):
		self.__jugadores.append(value)