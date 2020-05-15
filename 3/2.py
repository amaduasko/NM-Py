import sympy as sp
import numpy as np
import math

NN = 5
x = [0, math.pi / 6, math.pi / 4, math.pi / 3]
n = len(x)
X = sp.symbols('x', Float=True)
L = 0


def f(element):
    return math.tan(element)


def w(index):
    ww = 1
    for g in range(n):
        if g != index:
            ww *= X - x[g]
    return ww


y = np.zeros(n)
for i in range(n):
    y[i] = f(x[i])

for i in range(n):
    L += y[i] * w(i) / (w(i).subs(X, x[i]))
    print(L)

print(L)
print(sp.simplify(L))

print(y)
for i in x:
    print(L.subs(X, i))
