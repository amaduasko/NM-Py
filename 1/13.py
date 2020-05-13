import numpy as np

NN = 5
i = 1j
j = 1.5 + 0.1 * NN
A = np.array([[1 - j * i, 0, -j * i],
              [-j - 2 * i, -j * i, 2 + j * i],
              [i, 2, j]])
print("Matrix A")
print(A)
print()

b = np.array([1 + j - 3 * j * i,
              3 * j + 4 + 2 * j * i,
              2 * j + (j - 1) * i])
print(b)

Ar = A.real
Ai = A.imag
print("A real")
print(Ar)

print("A imag")
print(Ai)

br = b.real
bi = b.imag

n = 3

C = np.zeros((2 * n, 2 * n))
d = np.zeros(2 * n)
for i in range(n):
    d[i] = br[i]
    d[i + 3] = bi[i]
    for j in range(n):
        C[i, j] = Ar[i, j]
        C[i, j + 3] = -Ai[i, j]
        C[i + 3, j] = Ai[i, j]
        C[i + 3, j + 3] = Ar[i, j]
print(C)
print("d")
print(d)
y = np.zeros(2 * n)

y = np.linalg.solve(C, d)
print(y)
x = np.zeros(n, dtype=complex)
for i in range(n):
    x[i] = y[i] + 1j * y[i + 3]

print(f'x = {x}')
print("Ax = b")
print(np.dot(A, x))
