import numpy as np
import array as array

nombre=[]
rut=[] 

for i in range(0,5):
    
    i=input('ingresa los nombre:')
    nombre.append(i)
   
for j in range(0,5):
        
        j=int(input('ingresa el rut:'))
        rut.append(j)

nombre=np.sort(np.array(nombre))
rut=np.sort(np.array(rut))
print(f'orden alfabeticamente: {nombre}')
print(f'orden alfabeticamente: {rut}')



nombre=nombre[::-1]
rut=rut[::-1]
print(f'la otra manera: {nombre}')

print(f'la otra manera: {rut}')
