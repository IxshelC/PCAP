# Ejemplo 1 - Itera a través de los elementos de una tupla con un bucle

tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)

#-------------------#

# Ejemplo 2 - Verifica sí un elemento o no está presente en la tupla

tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)


#-------------------#

# Ejemplo 3 -Emplea la función len() para verificar cuantos elementos existen en la tupla

tuple_3 =(1,2,3,5)
print(len(tuple_3))


#-------------------#

# Ejemplo 4 - Unir o multiplicar tuplas

tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2

print(tuple_4)
print(tuple_5)