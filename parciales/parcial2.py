import json

class Pieza:
	def __init__(self, id,nombre):
		self.id = id
		self.nombre = nombre
	@property
	def id(self):
		return self.__id
	@id.setter
	def id(self, value):
		self.__id=value
	@property
	def nombre(self):
		return self.__nombre
	@nombre.setter
	def nombre(self, value):
		self.__nombre=value
	def __str__(self):
		toret=str.format("id: {0},nombre: {1}",self.id,self.nombre)
		return toret

class dictPiezas(object):
	def __init__(self,p):
		self.dict = dictPiezas.load(self)
	def addPieza(self,pieza):
		self.dict[pieza.id]=pieza.nombre
	def save(self):
		with open("piezas.dat", "w") as f:
			json.dump(self.dict, f)
	def load(self):
		with open("piezas.dat", "r") as f:
			self.dict = json.load(f)
		return self.dict


def obj2str(obj):
	st=p.__class__.__name__+":\n"
	st+="\tMetodos:\n"
	for me in dir(obj):
		m=getattr(obj, me)
		if callable(m):
			st+="\t\t"+me+"\n"
	st+="\tAtributos:\n"
	for me in dir(obj):
		m=getattr(obj, me)
		if not(callable(m)):
			st+="\t\t"+me+":"+str(m)+"\n"
	return st


fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])

piezza=Pieza(3,"Pieza3")
p={1:"Pieza",2:"Pieza2"}
d=dictPiezas(p)
d.save()
d.addPieza(piezza)
d.save()
l=d.load()
print(p)
print(l)
fibbo = lambda m: m if m<2 else fibbo(m-1)+fibbo(m-2)
cllaze = lambda m: map(lambda x: x/2 if x%2==0 else (x*3)+1, range(m))
print(range(10))
print(fib(10))
print(p.__class__.__name__)
print(obj2str(piezza))
print(cllaze(10))