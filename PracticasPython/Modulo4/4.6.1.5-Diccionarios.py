dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

# Imprimir valores aquí.
print(dictionary['gato'])           # Solo va imprimir "chat"
print(phone_numbers['Suzy'])        # Va imprimir el número de suszy



########

dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
words = ['gato', 'león', 'caballo']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")

