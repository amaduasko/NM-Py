import math

NN = 5


def f(x):
    return math.exp(-x) - x - 2


def f1(x):
    return -math.exp(-x) - 1


def f2(x):
    return math.exp(-x)


a, b = -3, 0

# (f(a) - f(xn))*(a - xn)
eps = 0.001


def hoard(first_element, second_element):
    xn = first_element
    xn1 = xn - f(xn) / (f(second_element) - f(xn)) * (second_element - xn)
    while abs(f(xn1)) > eps:
        xn = xn1
        xn1 = xn - f(xn) / (f(second_element) - f(xn)) * (second_element - xn)
    return xn1


print(f'f2(a) = {f2(a)}', '\n')
print(f'hoard(a, b) = {hoard(a, b)}', '\n')
print(f'f(hoard(a, b)) = {f(hoard(a, b))}', '\n')
