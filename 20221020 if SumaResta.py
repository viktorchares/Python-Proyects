# coding: utf-8
#Informática III P2_ACTIVIDAD_10:IF
#Viktor Chargoy Espino 5° E
#Suma o resta de 2 números

print("Selecciona la operación: 1. suma, 2. resta:")
print()
op=int(input("Operación:"))
print()
a=float(input("Da el valor del primer número:"))
print()
b=float(input("Da el valor del segundo número:"))
print()
res=float(0);

if (op==1):
    res=a+b;
elif(op==2):
    res=a-b;
print()

print("Resultado:", res)