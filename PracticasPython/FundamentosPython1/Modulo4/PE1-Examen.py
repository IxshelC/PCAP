# 1

# my_list = [1,2]
#
# for v in range(2):
#     my_list.insert(-1, my_list[v])
#
# print(my_list)

# Salida: [1,1,1,2]

## 2

# x = 1
# y = 2
# x , y, z = x, x, y
# z, y, z = x, y, z
#
# print(x, y, z)  # Salida: 1 1 2

## 3

# tup = (1, 2, 4, 8)
# tup = tup[-2:-1]
# tup = tup[-1]
# print(tup)  # Salida: 4

## 4

# dd = {"1": "0", "0":"1"}
# for x in dd.vals():
#     print(x, end="") # Salida: Error

## 5

# try:
#     print(5/0)
#     break
# except:
#     print("Lo siento, algo salió mal...")
# except (ValueError, ZeroDivisionError)
#     print("Mala suerte. . . ")  # Salida: SyntaxError

## 6
#
# a = 1
# b = 0
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print(a, b)     #Salida: 0 1

## 7

# def fun(inp=2, out=3):
#     return inp * out
#
# print(fun(out=2))       # Salida: 4


## 9

# my_list = [ x * x for x in range(5)]
#
# def fun(lst):
#     del lst[lst[2]]
#     return lst
#
# print(fun(my_list))  #Salida: [0, 1, 4, 9]

## 10

# i = 0
# while i < i + 2:
#     i += 1
#     print("*")
# else:
#     print("*") # Salida : infinito *


## 11

# x = 1 // 5 + 1 / 5
# print(x) # Salida: 0.2

## 14

# def function_1(a):
#     return None
#
# def function_2(a):
#     return function_1 (a) * function_1 (a)
#
# print(function_2(2))  # Salida: error


## 15

# print("a" , "b", "c", sep= "sep") #Saldia: asepbsepc

## 18

# lst = [[ x for x in range(3)]  for y in range(3)]
#
# for r in range(3):
#     for c in range(3):
#         if lst[r] [ c] %2 != 0:
#             print("#")      #Salida: ###



## 19

# x = int(input())
# y = int(input())
#
# x = x % y
# x = x % y
# y = y % x
# print(y) # salida: 0


## 22

# dct = {}
# dct  ['1'] = (1, 2)
# dct  ['2'] = (2, 1)
#
# for x in dct.keys():
    # print(dct[x][1], end="") # Salida: 21


## 23

# def fun(x):
#     if x % 2== 0:
#         return 1
#     else:
#         return 2
#
# print(fun(fun(2))) # salida: 2

## 24

# x = float(input())
# y = float(input())
#
# print(y** (1 / x)) # salida: 2.0


## 25

# foo = (1, 2, 3)
# foo.index(0) # salida: valueerror


## 30

# def fun(x, y):
#     if x == y:
#         return X
#     else:
#         return fun ( x , y -1)
#
# print(fun(0,3)) # salida: error

## 31

# dct = {'one': 'two', 'three': 'one', 'two':'three'}
# v = dct['three']
#
# for k in range(len(dct)):
#     v = dct[v]
#
# print(v) # Salida: one

## 32
#
# def fun(a, b):
#     return b ** a
#
# print(fun(b=2, 2))  # Salida: error


## 33

