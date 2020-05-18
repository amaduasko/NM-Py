import math
import sympy as sp
import random
import numpy as np

NN = 6
k = NN % 2

a = 0
b = 1
h = 10


def w(index):
    ww = 1
    for g in range(n):
        if g != index:
            ww *= (x - X[g])
    return ww


def poly():
    L = 0

    for item in range(len(X)):
        L += (f(X[item]) * w(item)) / (w(item).subs(x, X[item]))

    return sp.simplify(L)


def f(element):
    return NN / 2 * (math.e ** (-element)) ** (1 / (k + 4)) * math.cos(element / (k + NN)) + math.pi * NN / 2


def f_1(element):
    return f(element[0]) * ((2 * element[0] - element[1] - element[2]) / ((element[1] + element[2]) / 2) * ((element[1] + element[2]) / 2) + ())


def H(index):
    return X[index] - X[index - 1]


def H_(index):
    return (H(index + 1) + H(index)) / 2


X = [0, 0.1, 0.25, 0.32, 0.47, 0.51, 0.62, 0.79, 0.8, 0.91]
print(X)

n = len(X)

x = sp.symbols('x', Float=True)

res = poly()

result = np.zeros(h - 3)

for i in range(1, len(X) - 2):
    a = X[i]
    result[i - 1] = res.subs(x, X[i - 1]) * (2 * a - X[i] - X[i + 1]) / (H(i) * (H(i) + H(i + 1))) \
                    - res.subs(x, X[i]) * (2 * a - X[i + 1] - X[i - 1]) / (H(i) * H(i + 1)) \
                    + res.subs(x, X[i + 1]) * (2 * a - X[i - 1] - X[i]) / ((H(i) + H(i + 1)) * H(i + 1))

for i in result:
    print(i)
print()

for i in range(2, len(X) - 1):
    print(sp.diff(res, x).subs(x, X[i - 1]))

print('------------------------------------------')

result_2 = np.zeros(7)

for i in range(1, len(X) - 2):
    result_2[i - 1] = 1 / H_(i) * ((res.subs(x, X[i + 1]) - res.subs(x, X[i])) / H(i + 1) - (
            res.subs(x, X[i]) - res.subs(x, X[i - 1])) / H(i))

for i in result_2:
    print(i)
print()

for i in range(2, len(X) - 1):
    print(sp.diff(sp.diff(res, x), x).subs(x, X[i - 1]))
