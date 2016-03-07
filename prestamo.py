class Prestamo:
	def __init__(self,nCuote,importe,interes):
		self.__nCuote=nCuote
		self.__interes=interes
		self.__importeTotal=importe+((importe*interes)/100)
		self.__cuota=self.__importeTotal/nCuote
	@property
	def cuota(self):
		return self.__cuota

	@property
	def nCuote(self):
		return self.__nCuote

	@nCuote.setter
	def nCuote(self, value):
		self.__nCuote=value

	@property
	def importeTotal(self):
		return self.__importeTotal

	@importeTotal.setter
	def importeTotal(self, value):
		self.__importeTotal=value

	@property
	def interes(self):
		return self.__interes

	@interes.setter
	def interes(self, value):
		self.__interes=value

	@property
	def cuote(self):
		return self.__cuota

	def paga_cuota(self):
		self.__nCuote=self.__nCuote-1
		self.__importeTotal=self.__importeTotal-self.__cuota

	def amortiza(self, x):
		self.__importeTotal=self.__importeTotal-x
		self.__cuota=self.__importeTotal/self.__nCuote	

	def get_num_cuotas(self):
		return self.__nCuote

	def __str__(self):
		return str.format("importe total {0},interes {1}, cuota {2}, numero cuotas {3}", self.importeTotal, self.interes,self.cuota,self.nCuote)



p1=Prestamo(10,1000,10)
print(p1)	