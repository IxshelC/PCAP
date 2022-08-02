# Ejercicio 2

def es_entero(dato):                # Función "es_entero"
    if type(dato) == int:           # Sí el tipo de dato es igual a entero . . .
        return True                 # Retorna True(verdadero)
    elif type(dato) == float:       # Si no, el tipo de dato es igual a flotante . . .
        return False                # Retorna en Falso

print(es_entero(5))                 # Entero = TRUE
print(es_entero(4.5))               # Flotante = FALSE
print(es_entero("4"))               # String = None