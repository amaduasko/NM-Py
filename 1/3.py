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
b = np.array([[-j + 0.05 * j * j],
              [-0.8 * j + 0.1 * j * j - 0.02 * l * j],
              [-10 + 0.03 * j * j - 0.1 * l * j],
              [-0.2 * k + 0.3 * j + 0.02 * j * j],
              [0.01 * k * j - 0.5 * k - 0.2 * j * j]])
print(b)
n = 5
L = np.identity(n, dtype=float)

U = np.zeros((n, n), dtype=float)

for i in range(0, n):
    for j in range(0, n):
        if i <= j:
            U[i][j] = A[i][j] - sum((L[i][k] * U[k][j]) for k in range(0, i))
        else:
            L[i][j] = (A[i][j] - sum((L[i][k] * U[k][j]) for k in range(0, j))) / U[j][j]
print("matrix L")
print(L)
print("matrix U")
print(U)

# print(np.dot(L,U),3)

y = np.zeros(5)
x = np.zeros(5)

for k in range(0, n):
    y[k] = b[k] - sum((L[k][j] * y[j]) for j in range(0, k))
print("y")
print(y)
print("Ly=b")
print(np.dot(L, y))

for k in range(n - 1, -1, -1):
    x[k] = (y[k] - sum((U[k][j] * x[j]) for j in range(k, n))) / U[k][k]
print("x")
print(x)
print("Ax = b")
print(np.dot(A, x))

detA = 1
for i in range(n):
    detA *= L[i, i] * U[i, i]

print("results below ")
print(f'detA = {detA}')
print(np.linalg.det(A))
