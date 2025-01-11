# coding: utf-8
#Informática III P2_ACTIVIDAD_13:IF
#Viktor Chargoy Espino 5° E
#Calculadora, suma, resta, multiplicaciòn o división de 2 números.

print("Selecciona la operación: 1. suma, 2. resta, 3.Producto, 4.Cociente:")
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
elif(op==3):
    res=a*b;
elif(op==4):
    res=a/b;
    

print()


print("Resultado:", res)