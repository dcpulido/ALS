
class base:
	def __init__(self,numero,tamano, precio):
		self.__numero=numero
		self.__tamano=tamano
		self.__precio=precio

	@property
	def nombre(self):
		return self.__nombre

	@property
	def numero(self):
		return self.__numero

	@numero.setter
	def numero(self, value):
		self.__numero=value
	@property
	def tamano(self):
		return self.__tamano

	@tamano.setter
	def tamano(self, value):
		self.__tamano=value

	@property
	def precio(self):
		return self.__precio

	@precio.setter
	def precio(self, value):
		self.__precio=value

class codo(base):
	def __init__(self,numero,tamano, precio):
		self.__nombre="codo"
		base.__init__(self,numero,tamano, precio)
	@property
	def nombre(self):
		return self.__nombre


	def __str__(self):
		return str.format("{3}, tamano {0},precio {1}, id {2}", self.tamano, self.precio, self.numero, self.nombre)

class tuberia(base):
	def __init__(self,numero,tamano, precio):
		self.__nombre="tuberia"
		base.__init__(self,numero,tamano, precio)
	@property
	def nombre(self):
		return self.__nombre


	def __str__(self):
		return str.format("{3}, tamano {0},precio {1}, id {2}", self.tamano, self.precio, self.numero, self.nombre)

class tuerca(base):
	def __init__(self,numero,tamano, precio):
		self.__nombre="tuerca"
		base.__init__(self,numero,tamano, precio)

	@property
	def nombre(self):
		return self.__nombre

	def __str__(self):
		return str.format("{3}, tamano {0},precio {1}, id {2}", self.tamano, self.precio, self.numero, self.nombre)

class inventario:
	def __init__(self):
		self.__numPiezas=0
		self.__numCodos=0
		self.__numTuercas=0
		self.__numTuberias=0
		xCodo=[]
		xTuberia=[]
		xTuerca=[]

		self.__dic={"codo":xCodo,"tuberia":xTuberia ,"tuerca":xTuerca}

	@property
	def dic(self):
		return self.__dic

	@property
	def numPiezas(self):
		return self.__numPiezas

	@numPiezas.setter
	def numPiezas(self, value):
		self.__numPiezas=value

	@property
	def numCodos(self):
		return self.__numCodos

	@numCodos.setter
	def numCodos(self, value):
		self.__numero=value

	@property
	def numTuercas(self):
		return self.__numTuercas

	@numTuercas.setter
	def numTuercas(self, value):
		self.__numTuercas=value

	@property
	def numTuberias(self):
		return self.__numTuberias

	@numTuberias.setter
	def numTuberias(self, value):
		self.__numTuberias=value

	def addCodo(self,codo):
		self.numCodos=self.numCodos+1
		self.dic["codo"].append(codo)

	def getCodoNumero(self,num):
		for cod in self.dic["codo"]:
			if cod.numero == num: return cod

	def addTuberia(self,tuberia):
		self.numTuberias=self.numTuberias+1
		self.dic["tuberia"].append(tuberia)

	def getTuberiaNumero(self,num):
		for cod in self.dic["tuberia"]:
			if cod.numero == num: return cod

t1=tuberia(1,2,2)
c1=codo(10,10,10)
c2=codo(10,10,10)
ino=inventario()
ino.addCodo(c1)
ino.addTuberia(t1)
ino.addCodo(c2)
print(ino.getCodoNumero(10))
print(ino.getTuberiaNumero(1))
