año = int(input("Introduce un año:"))

#
# Escribe tu código aquí.
#
if año < 1582:
    print("No dentro del período del calendario Gregoriano")
else:

    if año %4 != 0:
        print("Año común")
    elif año %100 !=0:
        print("Año Bisiesto")
    elif año %400 !=0:
        print("Año común")
    else:
        print("Año bisiesto")