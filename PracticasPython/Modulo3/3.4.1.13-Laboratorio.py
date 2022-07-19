# paso 1: Crear una lista vacía llamada "beatles"
import imp


Beatles = []    #Lista vacía
print("Paso 1:", Beatles)

# paso 2: Emplea el método append() para agregar los siguientes miembros de la banda a la lista John Lennon, Paul McCartney y George Harrison
Beatles.append("John Lenon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)

# paso 3: Emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.
for i in range (2):
   Beatles.append(input("Ingresa el otro integrante: "))
print("Paso 3:", Beatles)


# paso 4: Usa la instrucción del para eliminar Stu Stucliffe y Pete Best
del Beatles[4]
del Beatles[3]
print("Paso 4:", Beatles)

# paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista
Beatles.insert(0,"Ringo Star")
print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Fav", len(Beatles))