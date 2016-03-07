def getData():
	print("introduce valores")
	toret=''
	aux=' '
	while aux != 0:
		aux = input()
		toret += str(aux)
	return toret

def media(data):
	toret=0
	for i in range(0,len(data)):
		toret += int(data[i])
		aux=i
	return toret/aux-1

def mayor(data):
	toret=0
	for i in range(0,len(data)-1):
		if int(data[i]) > toret:
			toret = int(data[i])
	return toret

def menor(data):
	toret=mayor(data)
	for i in range(0,len(data)-1):
		if int(data[i]) < toret:
			toret = int(data[i])
	return toret

data=getData()
print("media:{0},mayor={1},menor={2}".format(media(data),mayor(data),menor(data)))