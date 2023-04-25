import random

fila = int(input("ingresa el numero de filas: "))
Columna = int(input("ingrsa el numero de columnas: "))

m1 = []
for i in range(fila):
  fila = []
  for j in range(Columna):
    elem = random.randint(0, 10)
    fila.append(elem)
  m1.append(fila)

k = int(input("Ingresa el escalar: "))


def scalar(m1, k):
  return m1 * k


print(f" La matriz al aplicar el escalar es\n {scalar(m1,k)}")
