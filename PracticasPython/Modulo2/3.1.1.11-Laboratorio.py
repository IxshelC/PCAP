ingreso = float(input("Introduce el ingreso anual:"))

#
# Escribe tu código aquí.
#
if ingreso < 85528:
    inpuesto=0.18*ingreso-556.02
else:
    inpuesto = 14839.02 + 0.32*(ingreso-85528)

inpuesto = round(inpuesto, 0)
if inpuesto < 0:
    inpuesto = 0.0
print("El impuesto es:", inpuesto, "pesos")
