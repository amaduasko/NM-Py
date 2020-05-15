import sympy as sp
import numpy as np
import math

NN = 6
X = [-2, -1, 0, 1]
Y = [-48, 34, 16, 30]
Y1 = [0, -44, 0, 20]
Y2 = [0, 86, 32, -22]

n = len(X)
x = sp.symbols('x')
m = 1 + 3 + 3 + 3


def H(index):
    return x ** index


A = np.zeros((m, m))
for i in range(m):
    A[0, i] = H(i).subs(x, X[0])
    A[1, i] = H(i).subs(x, X[1])
    A[2, i] = H(i).subs(x, X[2])
    A[3, i] = H(i).subs(x, X[3])
    A[4, i] = sp.diff(H(i), x).subs(x, X[1])
    A[5, i] = sp.diff(H(i), x).subs(x, X[2])
    A[6, i] = sp.diff(H(i), x).subs(x, X[3])
    A[7, i] = sp.diff(sp.diff(H(i), x), x).subs(x, X[1])
    A[8, i] = sp.diff(sp.diff(H(i), x), x).subs(x, X[2])
    A[9, i] = sp.diff(sp.diff(H(i), x), x).subs(x, X[3])
print(A)
b = np.array([Y[0], Y[1], Y[2], Y[3], Y1[1], Y1[2], Y1[3], Y2[1], Y2[2], Y2[3]])
a = np.linalg.solve(A, b)
print(a)

poly_H = 0
for i in range(m):
    poly_H += a[i] * H(i)
print(poly_H.subs(x, X[0]))
print(poly_H.subs(x, X[1]))
print(poly_H.subs(x, X[2]))
print(poly_H.subs(x, X[3]))
