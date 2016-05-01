from jugador import Jugador
from google.appengine.ext import ndb


class equipoEnt:
	def __init__(self,name,nameJug1,nameJug2):
		self.__name=name
		jugadores=Jugador.query()
		for jugador in jugadores:
			if jugador.name==nameJug1:
				self.__jugador1=jugador
			if jugador.name==nameJug2:
				self.__jugador2=jugador
	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		self.__name=value

	@property
	def jugador1(self):
		return self.__jugador1

	@jugador1.setter
	def jugador1(self, value):
		self.__jugador1=value

	@property
	def jugador2(self):
		return self.__jugador2

	@jugador2.setter
	def jugador2(self, value):
		self.__jugador2=value
