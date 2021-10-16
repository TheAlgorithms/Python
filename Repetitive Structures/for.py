#FOR

#El FOR de Python no es el clásico que existe en C++ o
#java, es un FOREACH.
#Significa que necesita de una lista para iterar
#Itera tantos elementos tenga la lista.

lista = [1,3,5,2,4,7,8,6,9]

#este for imprime pro pantalla los valores de la lista

for elemento in lista:

#En cada iteración ELEMENTO toma un valor de LISTA

print(elemento)

# ------------------------ FOR Y RANGE ------------------------

#Se usa en situaciones en el que queremos
# que un for itere cierta cantidad de veces.
#Funcionamiento
# Range crea una LISTA de acuerdo con sus parámetros
# En cada iteración i toma un valor de la LISTA

for i in range(10):
print(i)

# ------------------------ BREAK ------------------------

#Sentencia que permite Salir de un Bucle

for i in range(100):
print(i)
if i == 4:

#Cuando i tenga el valor de 4
break #Se rompe el bucle

# ------------------------ CONTINUE ------------------------

#Permite detener la iteración actual y
#continuar con la siguiente

for i in range(10)
if i == 5:
    
#cuando i tome el valor de 5
#Saltará a la siguiente iteración
#por lo tanto no se imprimirá su valor
continue
print(i)
