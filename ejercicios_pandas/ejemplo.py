import pandas as pd

#Crear una serie en panda
#si, el indice no es configurado va a generar un indice [0....,len(data) -1]
serie = pd.Series(['Rojo','Verde','Azu'])
print(serie)

frutas = pd.Series(['Manzana','Uva','Naranja','Mango'],index=['a','b','c','d'])
print(frutas)

d = {"a":1,"b":3,"c":5}
print(pd.Series(d))

print(frutas.loc[1])