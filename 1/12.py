import numpy as np


def func(A, b):
    n = 5
    L = np.identity(n, dtype=float)

    U = np.zeros((n, n), dtype=float)

    for i in range(0, n):
        for j in range(0, n):
            if i <= j:
                U[i][j] = A[i][j] - sum((L[i][k] * U[k][j]) for k in range(0, i))
            else:
                L[i][j] = (A[i][j] - sum((L[i][k] * U[k][j]) for k in range(0, j))) / U[j][j]
    y = np.zeros(5)
    x = np.zeros(5)

    for k in range(0, n):
        y[k] = b[k] - sum((L[k][j] * y[j]) for j in range(0, k))
    for k in range(n - 1, -1, -1):
        x[k] = (y[k] - sum((U[k][j] * x[j]) for j in range(k, n))) / U[k][k]
    return x


NN = 5
j = 1.5 + 0.1 * NN
k = j
l = k - 0.1
m = 1
A = np.array([[j * m, 0.5 * j, 0, 0.2 * l, 0],
              [0.5 * j, j, 0.3 * j, 0, 0.1 * l],
              [0, 0.3 * j, 10, -0.3 * j, 0.5 * l],
              [0.2 * k, 0, -0.3 * j, j, -0.1 * j],
              [0, 0.1 * k, 0.5 * k, -0.1 * j, j * m]])
print("Matrix A")
print(A)
n = 5

E = np.eye(5)
print(E)

a = np.ones((n, n))

for i in range(n):
    a[i] = func(A, E[i])

a = np.transpose(a)

print(f' a = {a}')

print(np.dot(A, a))
