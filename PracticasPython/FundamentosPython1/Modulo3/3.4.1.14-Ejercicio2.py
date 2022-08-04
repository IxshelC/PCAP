# Ejercicio 2

lst = [1, 2, 3, 4, 5]       # Lista
lst_2 = []                  # Lista 2 vacía
add = 0                     # Variable add

for number in lst:          # Ciclo For numero, en la lista
    add += number           # 0= 0 + 1 (número de la lista), 1=1+2 =3 , 3=3+3 = 6 , 6=6+4=10, 10=10+5=1
    lst_2.append(add)       # Lista dos agrega 1 número hasta el último

print(lst_2)                # Imprime lista dos
