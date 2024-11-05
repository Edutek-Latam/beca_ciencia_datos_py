import numpy as np
np_respuestas = np.genfromtxt('ejercicio_numpy.csv',delimiter=',',skip_header=1)
print(f"filas, columnas? {np_respuestas.shape}")
print(f"Cuantos elementos? {np_respuestas.size}")
print(f"Cuantas dimensiones? {np_respuestas.ndim}")

print(np_respuestas.ndim)

edad = np_respuestas[:,0].astype(np.int16)

min_edad = np.min(edad)
max_edad = np.max(edad)
media_edad = np.mean(edad)
mediana_edad = np.median(edad)
#moda_edad = np.mode(edad)

""" print(f"Edad Minima {min_edad}")
print(f"Edad Maxima {max_edad}")
print(f"Edad Media {media_edad}")
print(f"Mediana {mediana_edad}") """
#print(f"Moda {moda_edad}")
#Para obtener todas las filas y el indice 2 de las columnas
#altura2 = np_respuestas[:,2]
#print(altura2[altura2 < 3 ])
#print(edad.size)
pesos = np_respuestas[:,1]
print(pesos)
altura = np.where(np_respuestas[:,2] > 3, np_respuestas[:,2]/100,np_respuestas[:,2])
""" print(f"Altura Promedio  {np.mean(altura)}")
print(f"Altura Maxima  {np.max(altura)}")
print(f"Altura Minima {np.min(altura)}") """

imc = pesos / (altura ** 2)
print(imc.astype(np.int8))