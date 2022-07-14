word_without_vowels = ""

user_word= input("Ingresa una palabra:")        # Indicar al usuario que ingrese una palabray asignarla a la variable user_word.
user_word = user_word.upper()                   # Conviertiendo las letras en mayúsculas

for letter in user_word:                        # Bucle
    if letter in "AEIOU":                       # Se borran las vocales"A,E,I,O,U" que se ingresen en user_word
        continue
    word_without_vowels += letter               # word_without_vowels = word_without_vwowels + letter
print(word_without_vowels)                      # Imprimir la palabra asignada a word_without_vowels.


