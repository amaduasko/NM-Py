import sympy as sp
import numpy as np
import math

NN = 6
k = NN % 2
x = sp.symbols('x')


def f(x):
    return NN / 2 * sp.exp(-x) ** (1 / (k + 4)) * sp.cos(x / (k + NN)) + sp.pi * NN / 2


def f1_h(i):
    return (f(X[i + 1]) - f(X[i])) / (X[i + 1] - X[i])


N = 10
X = np.linspace(1, 2, N)
Y = np.zeros(len(X))

for i in range(len(X)):
    print(X[i], " | ", f(X[i]))
print()
print("f'(x)")
for i in range(N - 1):
    print(X[i], " | ", f1_h(i))

print()
print("sympy f'(x)")
for i in range(N - 1):
    print(X[i], " | ", float(sp.diff(f(x), x).subs(x, X[i])))


def f1_h2(i):
    return (f(X[i + 1]) - f(X[i - 1])) / (2 * X[i + 1] - 2 * X[i])


print()
print("f'(x) 2порядка")
for i in range(1, N - 1):
    print(X[i], " | ", f1_h2(i))

print()
print("sympy f'(x) 2порядка")
for i in range(1, N - 1):
    print(X[i], " | ", float(sp.diff(f(x), x).subs(x, X[i])))


def f2_h(i):
    return (f(X[i - 1]) - 2 * f(X[i]) + f(X[i + 1])) / ((X[i + 1] - X[i]) * (X[i + 1] - X[i]))


print("f''(x)")
for i in range(1, N - 1):
    print(X[i], " | ", f2_h(i))

print()
print("sympy f''(x)")
for i in range(1, N - 1):
    print(X[i], " | ", float(sp.diff(sp.diff(f(x), x), x).subs(x, X[i])))
