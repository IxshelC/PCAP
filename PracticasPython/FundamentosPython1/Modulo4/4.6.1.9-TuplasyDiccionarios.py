school_class = {}                       #crea un diccionario vacío para ingresar los datos: el nombre del alumno es empleado como clave, mientras que todas las calificaciones asociadas son almacenadas en una tupla (la tupla puede ser el valor de un diccionario, esto no es un problema).

while True:                                                      # Se ingresa un bucle infinito
    name = input("Ingresa el nombre del estudiante: ")           # Se lee el nombre del alumno
    if name == '':                                               # Si el nombre es una cadena vacía se corta el bucle
        break

    score = int(input("Ingresa la calificación del estudiante (0-10): "))       ## Se pide la calificación del estudiante (rango de 0 - 10)
    if score not in range(0, 11):                                               # Si la calificación no está entre el 0 y el 10 se termina el bucle
	    break

    if name in school_class:                                                  # si el nombre del estudiante ya se encuentra en el diccionario, se alarga la tupla asociada con la nueva calificación (observa el operador +=).
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):                                        # se itera a través de los nombres ordenados de los estudiantes.
    adding = 0                                                                 # inicializa los datos necesarios para calcular el promedio (sum y counter).
    counter = 0
    for score in school_class[name]:                                            #se itera a través de la tupla, tomado todas las calificaciones subsecuentes y actualizando la suma junto con el contador.
        adding += score
        counter += 1
    print(name, ":", adding / counter)                                          #se calcula e imprime el promedio del alumno junto con su nombre.