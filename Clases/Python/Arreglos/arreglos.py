import numpy as np

#guia rapida de array
edades= np.array(5)
edades=[20,15,13,14,19] 

#indice
posicion_array= edades[4]

#inmutable array

edades[4]=22

print(edades[4]==22)

#len 

print(len(edades))



# append
edades.append(21)

print(len(edades))

nuevo=np.array(2)
nuevo=[13,12]
edades.append(nuevo)
print(len(edades))
print(edades)

#cound
print(edades.count(13))



#insert


edades.insert(0,25)
print(edades)


#pop


