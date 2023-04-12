

# calcular el perimetro de una circunferencia

a=int(input("introduce el radio:"))

if a < 0:
    print("INGRESE UN RADIO MAYOR A CERO")
else:
    r=str(2*3.14*a)
    print(f"el perimetro es:{r}")