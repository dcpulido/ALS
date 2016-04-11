#functools
#map aplica una funcion a todos los elementos de una lista
#filter devueve los elementos de una lista q cumplen una condicion o fuiltro
#reduce devuelve el resultado de aplicar fn a una lista
car= lambda l: None if l== None or l==[] else l[0]
cdr= lambda l: [] if l == None or l == [] else l[1:]

map = lambda l, f: [] if car(l) == None else \
		[f(car(l))] + map(cdr(l),f)

print(map([1,2,3],doble))


filter = lambda l, f: [] if car(l) == None else \
		[car(l)]+filter(cdr(l),f) if f(car(l)) else \
		filter(l,f)

print(filter([1,2,3],lambda x: x%2==0))

reduce = lambda l, f: car(l) if car(cdr(l)) == None else \ 
		f(car(l), reduce(cdr(l),f))
