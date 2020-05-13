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


def F(x, y):
    return f1(x, y) * f1(x, y) + f2(x, y) * f2(x, y)


def F_x(x, y):
    return 2 * f1(x, y) * f1_x(x, y) + 2 * f2(x, y) * f2_x(x, y)


def F_y(x, y):
    return 2 * f1(x, y) * f1_y(x, y) + 2 * f2(x, y) * f2_y(x, y)


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


x0 = 2
y0 = 1
i = 1
eps = 0.0001
alfy = 0.01
xn = x0 - alfy * F_x(x0, y0)
yn = y0 - alfy * F_y(x0, y0)
while F(xn, yn) > 2 * eps * eps:
    i += 1
    x0 = xn
    y0 = yn
    xn = x0 - alfy * F_x(x0, y0)
    yn = y0 - alfy * F_y(x0, y0)

print(f'xn = {xn}')
print(f'yn = {yn}')
print(f'f1(xn, yn) = {f1(xn, yn)}')
print(f'f2(xn, yn) = {f2(xn, yn)}')
print(f'i = {i}')
