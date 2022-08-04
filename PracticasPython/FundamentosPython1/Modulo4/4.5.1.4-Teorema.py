# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b                # la suma de a + b es mayor que c y la suma de b + c es mayor que a y la suma de c + a es mayor que b
#
#
# a = float(input('Ingresa la longitud del primer lado: '))
# b = float(input('Ingresa la longitud del segundo lado: '))
# c = float(input('Ingresa la longitud del tercer lado: '))
#
# if is_a_triangle(a, b, c):
#     print('Si, si puede ser un triángulo.')
# else:
#     print('No, no puede ser un triángulo.')


########### Teorema #########

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2


print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))

