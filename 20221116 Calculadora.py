# coding: utf-8
#Informática III P2_ACTIVIDAD_ Proyecto
#Equipo 5E
#Chargoy Espino Viktor #9
#Santiago Velasco Héctor #22
#Tlachi Celorio Maria José #23
#Vázquez García Yael Alejandro #25
#Calculadora de suma, resta, multiplicación, división o potencia de 2 números y raíz cuadrada de un número.

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicación(a,b):
    return a*b
def división(a,b):
    if(b==0):
        print("error")
        return 0
    res=a/b
    print("Resultado:", res)
    return a/b
def potencia(a,b):
    return a**b
def raíz(c):
    if(c<0):
        print("error")
        return 0
    res=c**(1/2)
    print("Resultado:", res)
    return c**(1/2)

print("Selecciona la operación: 1. suma, 2. resta, 3.multiplicación, 4.división,5.potencia,6.raíz cuadrada de 2 números:")
print()
op=int(input("Operación:"))
print(op)
a=float(input("Da el valor del primer número:"))
print(a)
if(op!=6):
    b=float(input("Da el valor del segundo número:"))
    print(b)
res=float(0);

if (op==1):
    res=suma(a,b)
    print("Resultado:", res)
elif(op==2):
    res=resta(a,b)
    print("Resultado:", res)
elif(op==3):
    res=multiplicación(a,b)
    print("Resultado:", res)
elif(op==4):
    res=división(a,b)
elif(op==5):
    res=potencia(a,b)
    print("Resultado:", res)
elif(op==6):
    res=raíz(a)

print()