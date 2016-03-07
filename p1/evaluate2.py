def getData():
	print("introduce datos en el formato apropiado")
	st=input()
	toret=st.split(' ')
	return toret

def evaluate(lst):
	if(len(lst)==1):return int(lst[0])
	if((lst[2]=="+") | (lst[2]=="-") & (lst[2]==lst[1])):
		if(lst[2]=="+"):return int(lst[0])+1
		if(lst[2]=="-"):return int(lst[0])-1
	op=lst[0]
	if(lst[1]==op):
		if(op=="+"):
			return int(lst[2])+1
		if(op=="-"):
			return int(lst[2])-1			
	else:
		n1=lst[1]
		n2=evaluate(lst[2:len(lst)])
		if(op=="+"):
			return int(n1)+n2
		if(op=="-"):
			return int(n1)-n2
		if(op=="*"):
			return int(n1)*n2
		if(op=="/"):
			return int(n1)/n2

print("resultado=: " +str(evaluate(getData())) )