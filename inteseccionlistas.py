#pasar lista por parametro , para separar elementos ; para separar listas, sin espacios
import sys
listas=sys.argv[1].split(";")
l1=listas[0].split(",")
l2=listas[1].split(",")
for i in l1:
	for k in l2:
		if(int(i)==int(k)):
			print(i)

