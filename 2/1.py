import math

NN = 5


def f(x):
    return math.exp(-x) - x - 2


a, b = -3, 0
eps = 0.00001
while (b - a) > eps:
    c = (a + b) / 2.0
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

print(f'c = {c}', '\n')
print(f'f(c) = {f(c)}')
