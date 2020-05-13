import math

NN = 5


def f(element):
    return math.exp(-element) - element - 2


def f1(element):
    return -math.exp(-element) - 1


def f2(element):
    return math.exp(-element)


def fi(element):
    lam = 1 / f1(a)
    return element - lam * f(element)


a, b = -3, 0

eps = 0.000001

x0 = -3

x = fi(x0)

while abs(x - x0) > eps:
    x0 = x
    x = fi(x0)

print(f'x = {x}')
print(f'f(x) = {f(x)}')
