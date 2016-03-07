#fibonacci

def fibonacci(x):
	a=0
	b=1
	if x==0:
		print(a)
	elif x==1:
		print(b)
	else:
		print(a)
		print(b)
		for i in range(2,x+1):
			aux=a+b
			a=b
			b=aux
			print(aux)

print("fibonacci de cuanto: ")
z=int(input())
fibonacci(z)
