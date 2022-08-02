# Ejercicio 4

def lista_actualizada(list):            # Función
    upd_lista =[]                       # Lista vacía
    for elem in list:                   # Para el elem en el argumento list
        elem **= 2                      # elem = elem al cuadrado
        upd_lista.append(elem)          # Se va agregando en la lista vacía
    return upd_lista                    # Retorna a la lista vacía

foo = [1,2,3,4,5]
print(lista_actualizada(foo))