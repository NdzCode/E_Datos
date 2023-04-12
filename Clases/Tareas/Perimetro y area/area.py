# calculando el area de la circunferencia

a=int(input("ingresa el radio:"))

if a < 0:
    print("Ingresa un numero mayor a cero")
else:
    c=str(3.14*a**2)
    print(f"El area de la circunferencia de {c}")