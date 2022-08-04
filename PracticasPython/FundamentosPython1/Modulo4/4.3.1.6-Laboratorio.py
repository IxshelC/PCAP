"""Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que
tambeien sea divisible por 400"""

def es_año_bisiesto (año) :
  if año % 4 != 0:
    return False
  elif año % 100 != 0:
    return True
  elif año % 400 != 0:
    return False
  else:
    return True

prueba_datos = [1900, 2000, 2016, 1987]
resultados_prueba = [False, True, True, False]
for i in range(len(prueba_datos)):
	yr = prueba_datos[i]
	print(yr,"->",end="")
	result = es_año_bisiesto(yr)
	if result == resultados_prueba[i]:
		print("OK")
	else:
		print("Fallido")