
#no olvidarse del SELF

class Punto:
	org_x=0
	org_y=0

	#metodo statico puedes invocarlo sin instancir el objeto
	@staticmethod
	def get_org():
		return Punto(Punto.org_x, Punto.org_y)

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

	#gracias a este metodo la clase soporta el operador ==
	def __eq__(self, p2): 
		return(self.x==p2.x and self.y==p2.y)

	def __neq__(self, p2): 
		return(not(self.__eq__(p2)))

	def __str__(self):
		return str.format("{0}, {1}", self.x, self.y)





p1=Punto(5, 6)
p2=Punto(5, 6)
p3=Punto(6, 6)
print(isinstance(p1,Punto))
print(p1)
print(p2)
print(p3)
print(p1==p2)
print(p3==p2)

print(dir(p1))

for m_name in dir(p1):
	m=getattr(p1, m_name)
	if callable(m):
		print("mtx: "+ m_name)
	else:
		print("Atr: "+ m_name)