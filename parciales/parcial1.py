class Punto:
	org_x=0
	org_y=0

	def __init__(self,x,y):
		self.__x=x
		self.__y=y

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, value):
		self.__x=value

	@property
	def y(self):
		return self.__y

	@y.setter
	def y(self, value):
		self.__y=value
	def __eq__(self, p2): 
		return(self.x==p2.x and self.y==p2.y)

	def __neq__(self, p2): 
		return(not(self.__eq__(p2)))

	def __str__(self):
		return str.format("({0}, {1})", self.x, self.y)

class Linea:

	def __init__(self,pa,pb):
		self.__punto_a=pa
		self.__punto_b=pb
	@property
	def punto_a(self):
		return self.__punto_a

	@punto_a.setter
	def punto_a(self, value):
		self.__punto_a=value

	@property
	def punto_b(self):
		return self.__punto_b

	@punto_b.setter
	def punto_b(self, value):
		self.__punto_b=value
	def __str__(self):
		return str.format("linea entre ({0}), y ({1})", self.__punto_a, self.__punto_b)

class Poligono:
	__lLineas=[]
	def __init__(self,lista):
		for i in range(1, len(lista)):
			l=Linea(lista[i-1],lista[i])
			self.__lLineas.append(l)
		self.__lLineas.append(Linea(lista[len(lista)-1],lista[0]))
	@property
	def lLineas(self):
		return self.__lLineas

	@lLineas.setter
	def lLineas(self, value):
		self.__lLineas=value

	def __str__(self):
		aux="Poligono: "
		for k in range(0, len(self.__lLineas)):
			aux+=str.format("{0}",self.lLineas[k])
		return aux

class Estudiante:
	dni=""
	nombre=""
	email=""
	def __init__(self,n,e,d):
		self.__nombre=n
		self.__dni=d
		self.__email=e
	@property
	def nombre(self):
		return self.__nombre

	@nombre.setter
	def nombre(self, value):
		self.__nombre=value

	@property
	def dni(self):
		return self.__dni

	@dni.setter
	def dni(self, value):
		self.__dni=value

	@property
	def email(self):
		return self.__email

	@email.setter
	def email(self, value):
		self.__email=value

	def __str__(self):
		return str.format("Estudiante: nombre: {0}, dni: {1}, email: {2}", self.__nombre, self.__dni,self.__email)

class EstudianteErasmus(Estudiante):
	pais=""
	def __init__(self,n,e,d,p):
		self.__pais=p
		Estudiante.__init__(self,n,e,d)

	@property
	def pais(self):
		return self.__pais

	@pais.setter
	def pais(self, value):
		self.__pais=value

	def __str__(self):
		return str.format("{0}, pais: {1}", Estudiante.__str__(self), self.__pais)

class EstudianteNormal(Estudiante):
	provincia=""
	def __init__(self,n,e,d,p):
		self.__provincia=p
		Estudiante.__init__(self,n,e,d)

	@property
	def provincia(self):
		return self.__provincia

	@provincia.setter
	def provincia(self, value):
		self.__provincia=value

	def __str__(self):
		return str.format("{0}, provincia: {1}", Estudiante.__str__(self), self.__provincia)

def es_palindromo (str):
	for i in range(0,len(str)):
		if str[i]!=str[len(str)-i-1]: return False
	return True
def histograma(lista):
	for i in range(0,len(lista)):
		aux = lista[i]
		str=""
		if aux <= 0 : aux=1
		if aux >11: aux=11
		for k in range(0,aux):
			str+="*"
		print(str)
def inversa(lista):
	toret=[]
	for i in range(0, len(lista)):
		toret.append(lista[len(lista)-i-1])
	return toret


print(es_palindromo("raaddaar"))
lista=[1,4,-2,13]
histograma(lista)
print(inversa(lista))
p1=Punto(1,2)
p2=Punto(2,2)
p3=Punto(2,6)
p4=Punto(4,2)
print(p1)
l1=Linea(p1,p2)
print(l1)
lista2=[p1,p2,p3,p4]
pol=Poligono(lista2)
print(pol)

e1=Estudiante("david","sdgd@as","44497623Y")
e2=EstudianteErasmus("david","sdgd@as","44497623Y","España")
e3=EstudianteNormal("david","sdgd@as","44497623Y","Ourense")
print(e1)
print(e2)
print(e3)

