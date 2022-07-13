secret_number =1 #Número secreto

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
# Pedir número
numero = int(input("Ingresa un número:"))

# El ciclo se reptita hasta que el número ingresado sea igual al secreto.
while numero != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle! ")
    numero = int(input("Ingresa un número:"))
print("¡Bien hecho, muggle! Eres libre ahora")
