bloques = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
#
altura = 0
while bloques > altura:
    altura +=1
    bloques -= altura

print("La altura de la pirámide:", altura)