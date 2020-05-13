import numpy as np

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
b = np.array([[-j + 0.05 * j * j],
              [-0.8 * j + 0.1 * j * j - 0.02 * l * j],
              [-10 + 0.03 * j * j - 0.1 * l * j],
              [-0.2 * k + 0.3 * j + 0.02 * j * j],
              [0.01 * k * j - 0.5 * k - 0.2 * j * j]])
print(b)
n = 5

D = np.identity(n, dtype=float)
print(D)

S = np.zeros((n, n), dtype=float)

# print(np.dot(L,U),3)

for i in range(0, n):
    D[i][i] = np.sign(A[i][i] - sum((S[p][i] * S[p][i] * D[p][p]) for p in range(0, i)))
    S[i][i] = np.sqrt(abs(A[i][i] - sum((S[p][i] * S[p][i] * D[p][p]) for p in range(0, i))))
    for j in range(i, n):
        S[i][j] = (A[i][j] - sum((S[p][i] * D[p][p] * S[p][j]) for p in range(0, i))) / (D[i][i] * S[i][i])

    # print(S)
SS = S
St = np.transpose(SS)
# print(St)

y = np.zeros(5)
x = np.zeros(5)

StD = np.dot(St, D)
print(StD)
for k in range(0, n):
    y[k] = (b[k] - sum((StD[k][j] * y[j]) for j in range(0, k))) / StD[k][k]
print("y")
print(y)
print("StDy=b")
print(np.dot(StD, y))

for k in range(n - 1, -1, -1):
    x[k] = (y[k] - sum((S[k][j] * x[j]) for j in range(k, n))) / S[k][k]
print("x")
print(x)

print("Sx=y")
print(np.dot(S, x))

print("Ax = b")
print(np.dot(A, x))
