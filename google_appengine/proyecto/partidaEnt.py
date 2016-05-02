from equipo import Equipo
from google.appengine.ext import ndb


class partidaEnt:
	def __init__(self,name,nameEq1,nameEq2,estado,user_id):
		self.__name=name
		self.__estado=estado
		equipos=Equipo.query()
		for equipo in equipos:
			if equipo.name==nameEq1:
				self.__equipo1=equipo
			if equipo.name==nameEq2:
				self.__equipo2=equipo
		self.__user_id=user_id
	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		self.__name=value

	@property
	def equipo1(self):
		return self.__equipo1

	@equipo1.setter
	def equipo1(self, value):
		self.__equipo1=value

	@property
	def equipo2(self):
		return self.__equipo2

	@equipo2.setter
	def equipo2(self, value):
		self.__equipo2=value

	@property
	def estado(self):
		return self.__estado

	@estado.setter
	def estado(self, value):
		self.__estado=value

	@property
	def user_id(self):
		return self.__user_id

	@user_id.setter
	def user_id(self, value):
		self.__user_id=value
