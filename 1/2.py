import numpy as np

NN = 5
j = 1.5 + 0.1 * NN
k = j
l = k - 0.1
m = 1
Aa = np.array([[j * m, 0.5 * j, 0, 0.2 * l, 0],
               [0.5 * j, j, 0.3 * j, 0, 0.1 * l],
               [0, 0.3 * j, 10, -0.3 * j, 0.5 * l],
               [0.2 * k, 0, -0.3 * j, j, -0.1 * j],
               [0, 0.1 * k, 0.5 * k, -0.1 * j, j * m]])
print("Matrix A")
print(Aa)
b = np.array([-j + 0.05 * j * j,
              -0.8 * j + 0.1 * j * j - 0.02 * l * j,
              -10 + 0.03 * j * j - 0.1 * l * j,
              -0.2 * k + 0.3 * j + 0.02 * j * j,
              0.01 * k * j - 0.5 * k - 0.2 * j * j])
print(b)
n = 5

A = np.column_stack((Aa, b))
print("New matrix A")
print(A)
for i in range(0, n):
    d = A[i, i]
    for j in range(n + 1):
        A[i, j] = A[i, j] / d
    for k in range(i + 1, n):
        t = A[k, i]
        for m in range(0, n + 1):
            A[k, m] -= A[i, m] * t

for i in range(n - 1, -1, -1):
    for k in range(i - 1, -1, -1):
        l = A[k, i]
        for j in range(n, -1, -1):
            A[k, j] -= A[i, j] * l

print(A)
x = np.zeros(5)
for k in range(n):
    x[k] = A[k, 5]
print(f'x = {x}', '\n')
print("Ax = b")
print(np.dot(Aa, x))
