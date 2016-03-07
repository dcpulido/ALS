import math
def get_data():
	print("v1 op v2")
	return input()
def calculea(v1,op,v2):
	v1=float(v1)
	v2=float(v2)
	if op=='+':
		return v1+v2
	elif op=='-':
		return v1-v2
	elif op=='/':
		return v1/v2
	elif op=='*':
		return v1*v2
	elif op=='^':
		return math.pow(v1,v2)

datos=get_data()
datos=datos.split(" ")
v1=datos[0]
op=datos[1]
v2=datos[2]
result=calculea(v1,op,v2)
print("{0}{1}{2}={3}".format(v1,op,v2,result))

