import numpy as np
import sympy as sp

NN = 5
j = 1.5 + 0.1 * NN
k = l = NN
m = 1
A = np.array([[j * m, 0.5 * j, 0, 0.2 * l, 0],
              [0.5 * j, j, 0.3 * j, 0, 0.1 * l],
              [0, 0.3 * j, 10, -0.3 * j, 0.5 * l],
              [0.2 * k, 0, -0.3 * j, j, -0.1 * j],
              [0, 0.1 * k, 0.5 * k, -0.1 * j, j * m]])
print("Matrix A")
print(A)
Aa = A
y = np.ones(5)

Y = np.dot(A, y)
# print(Y)
lambda1 = Y[0] / y[0]

y = Y
Y = np.dot(A, y)
lambda2 = Y[0] / y[0]

eps = 0.0001
while abs(lambda1 - lambda2) > eps:
    lambda1 = lambda2
    y = Y
    Y = np.dot(A, y)
    lambda2 = Y[0] / y[0]

lambda0 = lambda2

print("max")
print(lambda0)

A = np.linalg.inv(A)
y = np.ones(5)
Y = np.dot(A, y)

lambda1 = Y[0] / y[0]

y = Y
Y = np.dot(A, y)
lambda2 = Y[0] / y[0]

eps = 0.001

while abs(lambda1 - lambda2) > eps:
    lambda1 = lambda2
    y = Y
    Y = np.dot(A, y)
    lambda2 = Y[0] / y[0]

print("min")
print(1 / lambda2)
print(Y / np.linalg.norm(Y))

print(np.linalg.eig(Aa))

lam = sp.symbols('lam', Float=True)
L = np.identity(5)
L = L * lam
print(f' L = {L}')
