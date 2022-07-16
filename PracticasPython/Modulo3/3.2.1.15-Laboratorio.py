# 3.2.1.15 LABORATORIO: Hipótesis de Collatz

c0 = int(input("Ingresa un número:"))
pasos =0
while c0 != 1:
    if c0 %2 == 0:
        c0 = int(c0 /2)
        print(c0)
    else:
        c0 = 3 * c0 +1
        print(c0)
    pasos += 1

print("Pasos = ", pasos)