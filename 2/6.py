import math

NN = 5
a = 1
b = math.pi / 2 - 1
c = 1
d = -0.5
e = 1
f = math.pi
g = 1
h = -3


def f1(x, y):
    return math.sin(a * x + b) + c * y + d


def f2(x, y):
    return math.cos(e * y + f) + g * x + h


def f1_x(x, y):
    return a * math.cos(a * x + b)


def f1_y(x, y):
    return c


def f2_x(x, y):
    return g


def f2_y(x, y):
    return -e * math.sin(e * y + b)


def G(x, y):
    return (-f1(x, y) - f1_y(x, y) * H(x, y)) / f1_x(x, y)


def H(x, y):
    return (-f2(x, y) * f1_x(x, y) + f2_x(x, y) * f1(x, y)) / (f1_x(x, y) * f2_y(x, y) - f2_x(x, y) * f1_y(x, y))


x0 = 0.1
y0 = 0.1

eps = 0.001
xn = x0 + G(x0, y0)
yn = y0 + H(x0, y0)
while abs(xn - x0) > eps or abs(yn - y0) > eps:
    x0 = xn
    y0 = yn
    xn = x0 + G(x0, y0)
    yn = y0 + H(x0, y0)

print(f'xn = {xn}')
print(f'yn = {yn}')
print(f'f1(xn, yn) = {f1(xn, yn)}')
print(f'f2(xn, yn) = {f2(xn, yn)}')
