palabra = input("Ingresa una palabra o ingresa la palabra secreta:")
psecreta = "chupacabra"

while palabra != psecreta:
    palabra=input("Ingresa una palabra o ingresa la palabra secreta:")
    if palabra == psecreta:
        break
print("¡Has dejado el bucle con éxito")