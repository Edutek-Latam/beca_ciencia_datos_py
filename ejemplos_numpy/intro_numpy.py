import numpy as np

lista_1 = [1,2,3,4,5]
lista_2 = [5,6,7,8,9]
lista_suma = []

#suma de dos listas
for i,_ in enumerate(lista_1):
    lista_suma.append(lista_1[i] + lista_2[i])
#print(lista_suma)


#print(lista_1 + lista_2)
#Crear un vector a partir de una lista
np_array1 = np.array(lista_1)
np_array2 = np.array(lista_2)
#Suma de dos vectores o arrelgos de numpy
#print(np_array1 + np_array2)


############### tipos de datos
"""
Python              Numpy    
int                 np.int64,np.int32, np.int16, np.int8
float               np.float64, np.float32,np.float16, np.float8  
bool                np.bool_    
str                 U<[8], <--- U= unicode, va a tomar el tamano de la cadema mas grande
"""
""" print(np_array1.dtype)

array_int= np.array([12,13,14,15],dtype=np.int8)
print(array_int.dtype)

array_float = np.array([1.2,1.15,3.14,4.8], dtype=np.float16)
print(array_float.dtype)

array_str = np.array(["rojo","verde","azul", "Hola Mundo"])
print(array_str.dtype)

array_bool = np.array([[True,False],[True,True],[False,False]],dtype=np.bool_)
print(array_bool.dtype)
print(array_bool.astype(np.int8))
 """
array_list = np.array(["rojo",12,1,5,True])
print(array_list)

array_list2 = np.array([12,23,3.0,True])
print(array_list2)