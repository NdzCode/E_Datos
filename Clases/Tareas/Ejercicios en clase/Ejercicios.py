
import numpy as np

#Ejercicio 1
#Escribir un programa que pida al usuario 
#una palabra y muestre por consola el nª de 
#veces que contiene cada vocal """
vocal = np.array(5)
vocal =["a","e","i","o","u"]

palabra=input("Ingreda una palabra: ")
j=len(vocal)

for i in range(0,5):

  print(f" La cantidad de {vocal[i]} es {palabra.count(vocal[i])}\n")
 





#Ejercicio 2
#crear un arreglo aletorio de tamaño entre 10 a 30, 
#inprime el arreglo creado y luego solicitar por consola
#la busqueda de un elemento en es especifico del arreglo
#creado. utilizando array
 

aleatorio=np.random.randint(10,30,19)

elemento=int(input("ingresa el numero a buscar"))

if elemento in aleatorio:
  print(f"\n{aleatorio.sort(elemento)}")
else:
  print( "\nNo se encontro el elemento")
