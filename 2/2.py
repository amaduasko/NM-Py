import math

NN = 5


def f(x):
    return math.exp(-x) - x - 2


def f1(x):
    return -math.exp(-x) - 1


a, b = -3, 0

eps = 0.001


def newton(first_element, second_element):
    x0 = (first_element + second_element) / 2
    xn = x0 - f(x0) / f1(x0)
    xn1 = xn - f(xn) / f1(xn)
    while abs(xn1 - xn) > eps:
        xn = xn1
        xn1 = xn - f(xn) / f1(xn)
        return xn1


print(f'newton(a, b) = {newton(a, b)}')

print(f'f(newton(a, b)) = {f(newton(a, b))}')
