class Persona:
	def __init__(self,nombre,edad):
		self.nombre=nombre
		self.edad=edad

	def __str__(self):
		return str.format("{0}{1}",self.nombre,self.edad)