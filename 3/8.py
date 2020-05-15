import sympy as sp
import numpy as np

NN = 6
xi = [-3, -1, 0, 3, 4]
yi = [-5, -1, -2, 0, 2]
n = len(xi) - 1


def solve(A, B):
    n = m + 1
    L = np.eye(n)
    U = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i <= j:
                U[i, j] = A[i, j] - sum((L[i, k] * U[k, j]) for k in range(i))
            if i > j:
                L[i, j] = (A[i, j] - sum((L[i][k] * U[k][j]) for k in range(j))) / U[j, j]
    y = np.zeros(n)
    for k in range(n):
        y[k] = B[k] - sum((L[k, j] * y[j]) for j in range(k))

    x = np.zeros(n)
    for k in range(n - 1, -1, -1):
        x[k] = (y[k] - sum((U[k, j] * x[j]) for j in range(k, n))) / U[k, k]

    return x


m = 1
S = [n + 1]
t = []

for i in range(1, n):
    S.append(sum(((xi[j]) ** i) for j in range(len(xi))))
    t.append(sum((yi[j] * (xi[j]) ** (i - 1)) for j in range(len(xi))))

A = []

for i in range(m + 1):
    x = []
    for j in range(i, i + 2):
        x.append(S[j])
    A.append(x)

x = sp.symbols('x', Float=True)

res = solve(np.array(A), t)

Q = 0

for i in range(len(res)):
    Q += ((x ** i) * res[i])
print(Q)
