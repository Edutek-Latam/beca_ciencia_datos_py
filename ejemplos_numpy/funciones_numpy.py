import numpy as np

lista_1 = [1,2,3,4,5]
lista_2 = [5,6,7,8,9]

#Crear vector o matriz llena de ceros
#filas,columnas
array_zeros = np.ones((3,4), dtype=np.int8)
print(array_zeros)

#shape devuelve cuantas columnas y filas tiene nuestro vector o matriz
print(array_zeros.shape)

#Muestra cuantos elementos tiene nuestro vector o matriz
print(array_zeros.size)

#Muestra el tipo de dato del vector o matriz
print(array_zeros.dtype.name)

#Cuantas dimensiones tiene
print(array_zeros.ndim)

#llena un vector con un rango de valores, el tecer numero es de cuanto es el incremento
print(np.arange(1,20,2))

#llena un vector en un rago, el tercer parametro es la cantidad de valors a generar entre ese rango
array_linspace = np.linspace(1,20,12)

print(array_linspace.astype(np.int8))