car= lambda l: None if l== None or l==[] else l[0]

cdr= lambda l: [] if l == None or l == [] else l[1:]

inversa = lambda l: [] if l==None or l==[] else inversa(cdr(l))+[car(l)] 


l1=[1,2,3,4]
print(l1)
print(inversa(l1))
