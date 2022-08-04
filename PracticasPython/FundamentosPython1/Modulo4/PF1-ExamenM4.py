def func_1(a):
    return a**a


def func_2(a):
    return func_1(a)  * func_1(a)

print(func_2(2))



# P3

# def fun(inp=2, out=3):
#     return inp * out
#
# print(fun(out=2))


# P8

# def func(a,b):
#     return a ** a
# print(func(2))


# P9

# try:
#     value = input("Ingresa un valor: ")
#     print(value/value)
# except ValueError:
#     print("Entrada incorrecta...")
# except ZeroDivisionError:
#     print("Entrada errónea....")
# except TypeError:
#     print("Entrada muy erronea...")
# except:
#     print("Buuu!")


# P10
#
# dic ={}
# lista = ['a','b','c','d']
#
# for i in range (len(lista)-1):
#     dic[lista[i]] = (lista[i],)
#
# for i in sorted(dic.keys()):
#     k = dic[i]
#     print(k)
#     # print(k['0'])
#     # print(k["0"])
#     # print(k[0])



## P11

# def any():
#     print(var + 1, end="")
#
# var = 1
# any()
# print(var)


# P12

# dic ={'uno': 'dos', 'tres':'uno','dos':'tres'}
# v= dic['uno']
#
# for k in range(len(dic)):
#     v = dic[v]
#
# print(v)

# P14

# def fun(x,y,z):
#     return x + 2* y + 3 *z
# print(fun(0, z=1, y= 3))


# P 15

# def f(x):
#     if x == 0:
#         return 0
#     return x + f(x-1)
#
# print(f(3))


#P 17

lista = ["mari","had", "a", "little", "lamb"]

def lista(lista):
    del lista[3]
    lista[3] = "ram"

print(lista(lista))
