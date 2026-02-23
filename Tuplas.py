""" Ejercicio
T = 1,3
print (type(T)) 

Tm = ("angelo","diaz",3)
print (type(Tm))

Tr= ("angelo","diaz",30)
Elementos = Tr[2]
print (Elementos)

Sub_tupla = Tr[1:3]
print (Sub_tupla)

Sub_tupla.count("angelo")
print (Sub_tupla.count("angelo"))

Tupla = (4,5,6)
A,B,C = Tupla
print (A)
"""

Mi_primera_tupla= (1,2,3)
print(Mi_primera_tupla[2])


info_ciudades = (("Buenos Aires", 3000000, "Argentina"),
("Madrid", 3200000, "España"), ("Tokio", 13929286, "Japón"))

info_ciudades[0][0]  
info_ciudades[0][1]  # Población de la primera ciudad
info_ciudades[0][2]  

Nombre1 = info_ciudades[0][0]# País de la primera ciudad
Pblacion1 = info_ciudades[0][1] # Población de la primera ciudad
País1 = info_ciudades[0][2] # País de la primera ciudad

print("La ciudad de ",Nombre1,"en",País1,"tiene",Pblacion1,"personas")