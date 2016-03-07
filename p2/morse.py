#A	· —	 	N	— ·	 	0	— — — — —
#B	— · · ·	 	Ñ	— — · — —	 	1	· — — — —
#C	— · — ·	 	O	— — —	 	2	· · — — —
#CH	— — — —	 	P	· — — ·	 	3	· · · — —
#D	— · ·	 	Q	— — · —	 	4	· · · · —
#E	·	 	R	· — ·	 	5	· · · · ·
#F	· · — ·	 	S	· · ·	 	6	— · · · ·
#G	— — ·	 	T	—	 	7	— — · · ·
#H	· · · ·	 	U	· · —	 	8	— — — · ·
#I	· ·	 	V	· · · —	 	9	— — — — ·
#J	· — — —	 	W	· — —	 	.	· — · — · —
#K	— · —	 	X	— · · —	 	,	— — · · — —
#L	· — · ·	 	Y	— · — —	 	 ?	· · — — · ·
#M	— —	 	Z	— — · ·	 	"	· — · · — ·	 	 !	— · — · — —
import sys
f = open (sys.argv[1],"rU")
lineas=f.readlines()
f.close

dic={".-":"a","-...":"b"}
pal=""
frase=""
for l in lineas:
	palabras = l.split("  ")
	for p in palabras:
		caracteres= p.split(" ")
		for c in caracteres:
			c=c.replace("\n","")
			pal+=dic[c]
		frase+=" "+pal
		pal=""
	print(frase)
	frase=""