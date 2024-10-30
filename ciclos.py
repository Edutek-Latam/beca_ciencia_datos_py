#Itera sobre una secuencia (como listas o rangos, etc.)
""" for i in range(5):
    print(i)
 """
#Ejecuta el bloque de codigo mientras una concicion es verdadera
""" n = 0
while n < 5:
    print(n)
    n+= 1
 """
#break: Termina o rompe un ciclo o bucle
""" for i in range(10):
    if i == 5:
        #pass
        break
    print(i)
 """
#continue: Salta a la siguiente iteracion del bucle
for i in range(5):
    if i == 2:
        continue
    print(i)
