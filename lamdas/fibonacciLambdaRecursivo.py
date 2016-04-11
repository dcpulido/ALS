aux = lambda m,p,a: p+a  if m==0 else aux(m-1,p+a,p) 
fibb = lambda m: aux(m-2,1,0) if m>2 else 0 if m==0 else 1

fibbo = lambda m: m if m<2 else fibbo(m-1)+fibbo(m-2)
print(fibb(3))
