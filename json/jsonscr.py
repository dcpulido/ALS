import json

num_alumnos={"ALS":30,"DIA":15,"DM":90}

 #str_num_alumnos=json.dump(num_alumnos)
#rint(str_num_alumnos)

#print(json.loads(str_num_alumnos))


#guardar
f=open("datos.txt","wt")
json.dump(num_alumnos,f)
f.close()

#recuperar

num_alumnos=None
f=open("datos.txt","rU")
num_alumnos=json.load(f)
print(num_alumnos)