import numpy as np

import random

# creando m1
fila = int(input("ingrese la cantidad de filas de la matriz :"))
columna = int(input("ingrese la cantidad de columnas :"))

m_1 = []

for i in range(fila):
  fila = []
  for j in range(columna):
    elem = random.randint(0, 5)
    fila.append(elem)
  m_1.append(fila)

# creando m2

fila = int(input("ingrese la cantidad de filas de la matriz :"))
columna = int(input("ingrese la cantidad de columnas :"))
m_2 = []

for i in range(fila):
  fila = []
  for j in range(columna):
    elem = random.randint(0, 5)
    fila.append(elem)
  m_2.append(fila)

# m_3 =suma de m1 y m2


def suma(m_1, m_2):
  m_3 = np.add(m_1, m_2)
  return m_3


m_3 = suma(m_1, m_2)

print(f"\nLa matriz resultado es: {suma(m_1,m_2)}")

# creando m4
m_4 = []

fila = int(input("ingrese la cantidad de filas de la matriz:"))
columna = int(input("ingrese la cantidad de columnas: "))

for i in range(fila):
  fila = []
  for j in range(columna):
    elem = random.randint(0, 5)
    fila.append(elem)
  m_4.append(fila)


def resta(m_3, m_4):
  m_suma = np.subtract(m_3, m_4)
  return m_suma


print(f"\nLa matriz resultado es: {resta(m_3,m_4)}")
