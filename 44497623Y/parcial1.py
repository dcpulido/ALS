class Palabra:
	def __init__(self,pal,may):
		M = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
		self.__palabra=pal
		if may == True:
			self.__palabra=str.format("{0}{1}",self.__palabra[0].upper(),self.__palabra[1, len(self.__palabra)])
	
	@property
	def mayuscula(self):
		return self.__mayuscula

	@mayuscula.setter
	def mayuscula(self, value):
		self.__mayuscula=value
		if value==True:
			lower(self.__palabra[0])
		else:
			upper(self.__palabra[0])
	@property
	def palabra(self):
		return self.__palabra

	@palabra.setter
	def palabra(self, value):
		self.__palabra=value

	def __str__(self):
		return self.__palabra









class TableroTetrix:
	def __init__(self):
		self.__filas=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
		for i in range(0,len(self.__filas)):
			for k in range(0,9):
				self.__filas[i].append(False)
	
	@property
	def filas(self):
		return self.__filas
	
	def set(self,f,c, value):
		self.__filas[f][c]=value


	def get(self,f,c):
		return self.__filas[f][c]

	def elmina_filas(self,f):
		flag=True
		for i in range(0,len(self.__filas[f])):
			if self.__filas[f][i]==False:flag=False
		if flag==True:
			for i in range(f,1,-1):
				self.__filas[i]=self.__filas[i-1]
			for k in range(0,9):
				self.__filas[0].append(False)



	def __str__(self):
		aux=""
		for i in range(0,len(self.__filas)):
			for k in range(0,9):		
				if self.__filas[i][k]==True: aux+="X"
				else: aux+=" "
			aux+="\n"
		return aux

def resta_conjuntos(con_a,con_b):
	toret=[]
	for i in range(0,len(con_a)):
		flag=True
		for k in range(0,len(con_b)):
			if con_b[k] % con_a[i]==0 :flag=False
		if flag==True : toret.append(con_a[i])
	return toret


def histograma(lista):
	for i in range(0,len(lista)):
		aux = lista[i]
		str=""
		while aux >10:
			aux=int(aux/10)
		for k in range(0,aux):
			str+="*"
		print(str)

def ordena(Lista):
	toret=[]
	max=0
	min=9999999999999999
	for i in range(0, len(lista)):
		if lista[i]<min:min=lista[i]
		if lista[i]>max:max=lista[i]
	toret.append(min)
	toret.append(max)
	for i in range(0, len(lista)):
		for k in range(1, len(toret)):
			if lista[i]<toret[k] and lista[i]>toret[k-1]: toret.insert(k,lista[i])
	return toret



lista=[10,4,-2,13,7,9,26]
lista2=[5,4,-2,13,8,6,4,6]
print(resta_conjuntos(lista2,lista))
lista=[10,5,8]
lista2=[100,50,80]
histograma(lista)
histograma(lista2)
lista=[10,4,-2,13,7,9,26]
print(ordena(lista))

t1= TableroTetrix()
print(t1.get(0,0))
t1.set(0,0,True)
t1.set(16,0,True)
for i in range(0,9):
	t1.set(5,i,True)
print(t1.get(0,0))
#print(t1)
t1.elmina_filas(5)
print(t1)

p1=Palabra("david",True)
#p1.mayuscula("False")
print(p1)