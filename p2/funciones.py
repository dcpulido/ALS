#funciones en python
#comentarios y documentacion para el IDE
"""Devuelve si un num x es par o no

	:param x: El num a considerar
	:return: True si es par False en otro caso
"""
#puedes definir funciones dentro de funciones
def es_par(x):
	def modulo(a, b):
		return a % b
#las funciones interiores tienen acceso a las variables de la funciones exteriores
	def calcula_modulo():
		return modulo(x,2)

	return calcula_modulo()==0


i=1
#operadores logicos and or y not no ! && y ||
while i<11:
	if es_par(i):
		print(i)
	else:
		print("impar")
	i += 1