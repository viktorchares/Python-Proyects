# coding: utf-8
#Informática III P2_ACTIVIDAD_11:IF
#Viktor Chargoy Espino 5° E
#Calcula la velocidad rectilínea de un móvil. V= d/t

print("Introduce los valores para calcular la velcidad:")
print()
d=float(input("Da el valor de la distancia:"))
print()
t=float(input("Da el valor del tiempo:"))
print()
v=float(0);

if (t==0):
    print("velocidad infinita")
else:
    v=d/t
    print("Velocidad:", v)
    
print()

