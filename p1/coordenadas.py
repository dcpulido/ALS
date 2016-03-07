def parse(x,y):
	return("("+str(x)+"),("+str(y)+")")
def parse2(x,y):
	return "({0}),({1})".format(x,y)

print("coordenada 1: ")
coor1=int(input())
print("coordenada 2: ")
coor2=int(input())
print(parse(coor1,coor2))
print(parse2(coor1,coor2))