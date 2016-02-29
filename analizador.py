import sys
import string

def ParsePuntuacion(str):
	l=list(str)
	for i in range(0,len(l)):
		try:
			if string.punctuation.index(l[i]) :
				del(l[i])
		except:
			pass
	return "".join(l)		

def ParsePalabra(str):
	l=str.split(" ")
	return l


f = open (sys.argv[1],"rU")
linea= " "
print(sys.argv[1])
while linea != None:
	linea=f.readline()
	print(linea)
	linea=ParsePuntuacion(linea)
	l=ParsePalabra(linea)
	print(linea)
f.close