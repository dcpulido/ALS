#elimina caracteres repetidos

import sys
f = open (sys.argv[1],"rU")
lineas=f.readlines()
f.close

for l in lineas:
	aux=""
	toret=""
	i=0
	for ch in l:
		if ch!=aux:
			toret+=ch
			i=i+1
			aux=ch
	print(toret)