"""Este programa es una interfaz gráfica que obtenga y muestre la conversión de una unidad a otra, ambas seleccionadas por el usuario. 
Tu programa debe ser capaz de convertir las siguientes unidades:
"Longitud", "Temperatura", "Masa", "Tiempo", "Velocidad", "Moneda"
Longitud de mm, cm o m a in, ft o yd.
Temperatura de °C, °F o K a °C, °F o K.
Masa de Kg o g a lb u oz.
Tiempo de s, min, hora a año, lustro, década.
Velocidad de km/min o km/h a mi/min o min/h.
Moneda: Peso, Dolar o Euro a Yen, Libra esterlina o Franco Suizo.
Ademas debe cumplir con los siguientes criterios:
Titulo de la ventana: "Conversor de Unidades"
Tamaño de ventana libre.
Color de fondo de la ventana personalizado (no el que da por default).
Una lista desplegable con su etiqueta para seleccionar el tipo de conversión.
Un botón con el mensaje "ACEPTAR" para elegir el tipo de conversión
Dos entradas, una para introducir la magnitud a convertir y otro donde se insertará la conversión.
Un botón con el mensaje "Convertir" para mostrar el resultado.
Todas las etiquetas deben tener el mismo color de fondo que la ventana y con un tipo de fuente diferente al que se da por default.
Todos los elementos deben estar correctamente distribuidos en la ventana, la ventana no debe tener grandes espacios libres.
Al seleccionar otro tipo de conversión se debe de borrar todos los widgets generados en la operación anterior.

Viktor Chargoy Espino #2 6B

Usar un string, comparar size entre los 2 y elegir !=0 con el get.
"""

import tkinter as tk
from tkinter import ttk

"""
def launo(var, index, mode):
  modo=False
def lados(var, index, mode):
  modo=True
"""
def convertir():

  str1=a.get()
  #str2=b.get()
  #print(str1,str2)
  if(str1!=""):
    modo=False
  else:
    modo=True
  #x = float(a.get())
  c = de.get()
  d = ah.get()
  if(modo==False):
    temp = float(a.get())
    r = float(34404)
    #print(temp,r,opcion,c,d)
    if opcion == "Longitud":  #En metros
      if (c == "mm"):
        temp = temp / 1000
      elif (c == "cm"):
        temp = temp / 100
  
      if (d == "in"):
        r = temp / 0.0254
      elif (d == "ft"):
        r = temp / 0.3048
      elif (d == "yd"):
        r = temp * 1.0936133
  
    elif opcion == "Temperatura":
      if (c == "ºF"):
        temp = (temp - 32) * 5 / 9
      elif (c == "K"):
        temp = temp - 273.15
  
      if (d == "ºC"):
        r = temp
      elif (d == "ºF"):
        r = (temp * 9 / 5) + 32
      elif (d == "K"):
        r = temp + 273.15
  
    elif opcion == "Masa":  #Gramos
      if (c == "Kg"):
        temp = temp * 1000
  
      if (d == "lb"):
        r = temp / 453.6
      elif (d == "oz"):
        r = temp / 28.35
    elif opcion == "Tiempo":  #en horas
      if (c == "s"):
        temp = temp / 3600
      elif (c == "min"):
        temp = temp / 60
  
      if (d == "año"):
        r = temp / 8760
      elif (d == "lustro"):
        r = temp / 43800
      elif (d == "decada"):
        r = temp / 87600
  
    elif opcion == "Velocidad":  #En km/h
      if (c == "km/min"):
        temp = temp * 60
  
      if (d == "mi/min"):
        r = temp / 96.561
      elif (d == "mi/h"):
        r = temp / 1.609
  
    elif opcion == "Moneda":  #En dólares
      if (c == "Peso"):
        temp = temp * 0.058
      elif (c == "Euro"):
        temp = temp * 0.92
  
      if (d == "Yen"):
        r = temp * 149.54
      elif (d == "Libra esterlina"):
        r = temp * 0.80
      elif (d == "Franco Suizo"):
        r = temp * 0.89
    b.delete(0, tk.END)
    b.insert(0, f"{r:.3f}")
  else:
    temp = float(b.get())
    r = float(34404)
    #print(temp,r,opcion,c,d)
    if opcion == "Longitud":  #En metros
      if (d == "in"):
        temp = temp * 0.0254
      elif (d == "ft"):
        temp = temp * 0.3048
      elif (d == "yd"):
        temp = temp / 1.0936133
      
      if (c == "mm"):
        r = temp * 1000
      elif (c == "cm"):
        r = temp * 100
      else:
        r=temp


    elif opcion == "Temperatura":#C
      if (d == "ºF"):
        temp = (temp - 32) * 5 / 9
      elif (d == "K"):
        temp = temp - 273.15
      
      if (c == "ºF"):
        r = (temp * 9 / 5) + 32
      elif (c == "K"):
        r = temp + 273.15
      else:
        r=temp

      

    elif opcion == "Masa":  #Gramos
      if (d == "lb"):
        temp = temp * 453.6
      elif (d == "oz"):
        temp = temp * 28.35

      if (c == "Kg"):
        r = temp / 1000
      else:
        r=temp

        
    elif opcion == "Tiempo":  #en horas
      if (d == "año"):
        temp = temp * 8760
      elif (d == "lustro"):
        temp = temp * 43800
      elif (d == "decada"):
        temp = temp * 87600

      if (c == "s"):
        r = temp * 3600
      elif (c == "min"):
        r = temp * 60
      else:
        r=temp

      
    elif opcion == "Velocidad":  #En km/h
      if (d == "mi/min"):
        temp = temp * 96.561
      elif (d == "mi/h"):
        temp = temp * 1.609

      if (c == "km/min"):
        r = temp / 60
      else:
        r=temp


    elif opcion == "Moneda":  #En dólares
      if (d == "Yen"):
        temp = temp / 149.54
      elif (d == "Libra esterlina"):
        temp = temp / 0.80
      elif (d == "Franco Suizo"):
        temp = temp / 0.89

      if (c == "Peso"):
        r = temp / 0.058
      elif (c == "Euro"):
        r = temp / 0.92
      else:
        r=temp
        
    a.delete(0, tk.END)
    a.insert(0, f"{r:.3f}")


def menu():
  global de, ah, a, b, opcion, c, d,ast,bst
  #global a,b,c,d
  #ast=tk.StringVar()
  #bst=tk.StringVar()
  for widget in window.winfo_children():
    if widget.winfo_y() > 100 and widget.winfo_y() < 250:
      widget.destroy()
  
  a = ttk.Entry(justify="right",font=("Arial", 8))  #entrada de texto, caja de registro , textvariable=ast
  a.place(x=20, y=150, width=100)  #colocar caja con coordenadas
  b = ttk.Entry(justify="right",
                font=("Arial", 8))  #entrada de texto, caja de registro , textvariable=bst
  b.place(x=200, y=150, width=100)  #colocar caja con coordenadas

  #ast.trace_add("write", callback=launo)
  #bst.trace_add("write", callback=lados)

  #print(modo)
  opcion = op.get()
  if opcion == "Longitud":
    de = ttk.Combobox(state="readonly",
                      values=["mm", "cm", "m"],
                      font=("Arial", 8))
    de.place(x=140, y=150, width=40)
    ah = ttk.Combobox(state="readonly",
                      values=["in", "ft", "yd"],
                      font=("Arial", 8))
    ah.place(x=340, y=150, width=40)

  elif opcion == "Temperatura":
    de = ttk.Combobox(state="readonly",
                      values=["ºC", "ºF", "K"],
                      font=("Arial", 8))
    #Solo puede seleccionar, poner opciones en values entre corchetes
    de.place(x=140, y=150, width=40)
    ah = ttk.Combobox(state="readonly",
                      values=["ºC", "ºF", "K"],
                      font=("Arial", 8))
    ah.place(x=340, y=150, width=40)
  elif opcion == "Masa":
    de = ttk.Combobox(state="readonly", values=["Kg", "g"], font=("Arial", 8))
    de.place(x=140, y=150, width=40)
    ah = ttk.Combobox(state="readonly", values=["lb", "oz"], font=("Arial", 8))
    ah.place(x=340, y=150, width=40)
  elif opcion == "Tiempo":
    de = ttk.Combobox(state="readonly",
                      values=["s", "min", "hora"],
                      font=("Arial", 8))
    de.place(x=140, y=150, width=40)
    ah = ttk.Combobox(state="readonly",
                      values=["año", "lustro", "decada"],
                      font=("Arial", 8))
    ah.place(x=340, y=150, width=50)
  elif opcion == "Velocidad":
    de = ttk.Combobox(state="readonly",
                      values=["km/min", "km/h"],
                      font=("Arial", 8))
    de.place(x=140, y=150, width=50)
    ah = ttk.Combobox(state="readonly",
                      values=["mi/min", "mi/h"],
                      font=("Arial", 8))
    ah.place(x=340, y=150, width=50)
  elif opcion == "Moneda":
    de = ttk.Combobox(state="readonly",
                      values=["Peso", "Dolar", "Euro"],
                      font=("Arial", 8))
    de.place(x=140, y=150, width=50)
    ah = ttk.Combobox(state="readonly",
                      values=["Yen", "Libra Esterlina", "Franco Suizo"],
                      font=("Arial", 8))
    ah.place(x=340, y=150, width=100)

  button = tk.Button(text="CONVERTIR", font=("Arial", 8), command=convertir)
  button.place(x=300, y=40)


window = tk.Tk()
window.title("Conversor de unidades")
window.geometry("500x300")
window.config(bg="azure")  #Color de fondo la ventana con config

global modo
modo=bool(0)

hello = tk.Label(text="Conversor de unidades", bg="azure", font=("Arial", 12))
hello.pack()

for widget in window.winfo_children():
  if widget.winfo_y() > 100 and widget.winfo_y() < 250:
    widget.destroy()

csignos = tk.Label(text="Selecciona la conversión a realizar y presiona aceptar: ", bg="azure", font=("Arial", 8))  #etiqueta, titulo en pantalla
csignos.place(x=10, y=20)

#Combobox listas desplegables
#colocaop = tk.Label(text="",bg="azure",font=("Arial",8)) #etiqueta, titulo en pantalla
#colocaop.place(x=20, y=30)
op = ttk.Combobox(state="readonly", values=["Longitud", "Temperatura", "Masa", "Tiempo", "Velocidad", "Moneda"])
#Solo puede seleccionar, poner opciones en values entre corchetes
op.place(x=40, y=50, width=100)

button = tk.Button(text="ACEPTAR", font=("Arial", 8), command=menu)
button.place(x=200, y=40)

instrucciones = tk.Label(text="Ingresa la cantidad, junto la unidad de origen y luego la unidad de destino", bg="azure", font=("Arial", 8))  #etiqueta, titulo en pantalla
instrucciones.place(x=10, y=80)
instrucciones2 = tk.Label(text="Luego presiona convertir", bg="azure", font=("Arial", 8))  #etiqueta, titulo en pantalla
instrucciones2.place(x=10, y=100)

tk.mainloop()
