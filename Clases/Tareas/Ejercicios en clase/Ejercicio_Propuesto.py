


a=int(input("ingresa el numero entero:"))

def decimal_binario(a):
    num_binario=[]
    
    while a >=1:
        num_binario.append(a%2)
        a=int(a/2)
    return num_binario[::-1]

print(f"La conversion del  entero {a} al binario es :",decimal_binario(a))