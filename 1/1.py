import numpy as np

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
C = np.copy(A)
b = np.array([[-j + 0.05 * j * j],
              [-0.8 * j + 0.1 * j * j - 0.02 * l * j],
              [-10 + 0.03 * j * j - 0.1 * l * j],
              [-0.2 * k + 0.3 * j + 0.02 * j * j],
              [0.01 * k * j - 0.5 * k - 0.2 * j * j]])
print(b)
n = 5
for k in range(0, n - 1):
    for i in range(k + 1, n):
        b[i] -= A[i][k] / A[k][k] * b[k]
        for j in range(n - 1, k - 1, -1):
            A[i][j] -= A[i][k] / A[k][k] * A[k][j]
print("New matrix A")

print(A)
print("New b")
print(b)
x = np.zeros(5)

x[n - 1] = (b[n - 1]) / A[n - 1][n - 1]
for k in range(n - 2, -1, -1):
    x[k] = (b[k] - sum((A[k][j] * x[j]) for j in range(k + 1, n))) / A[k][k]
print("x")
print(x)
print("Ax = b")
print(np.dot(C, x))

detA = 1
for i in range(n):
    detA *= A[i, i]

print(" loading results below : ", '\n')
print(f'detA = {detA}')
print(np.linalg.det(A))
