import sys

f = open (sys.argv[1],"rU")
lineas=f.readlines()
f.close
dic=dict()
for l in lineas:
	partes = l.split("|")
	i=0
	for ch in partes[0]:
		dic[i]=ch
		i=i+1
	#nums=partes[1].replace("  ","")
	nums=partes[1]
	nums=nums.split()
	for n in nums:
		#n.replace("\n","")
		print(dic[int(n)-1])
