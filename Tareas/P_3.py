

a=float(input("Igresa el valor de los catetos en orden:"))
b=float(input("Igresa el valor de los catetos en orden:"))
c=float(input("Igresa el valor de los catetos en orden:"))

perimetro=(a+b+c)
s=(perimetro/2)
area=float((s*((s-a)*(s-b)*(s-c))))**0.5

print(f"El perimetro del triangulo es {perimetro} y el area de este es {area}" )