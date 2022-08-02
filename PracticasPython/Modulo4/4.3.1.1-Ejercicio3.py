# Ejerccio 3

def even_num_lst(ran):              # Función
    lst=[]                          # Lista vacía
    for num in range(ran):          # Para num en rango (ran)
        if num % 2 == 0:            # Si el número dividido entre 2 da a 0
            lst.append(num)         # En la lista vacía se va agregando el número
    return lst

print(even_num_lst(11))            # El rango es hasta 11 números