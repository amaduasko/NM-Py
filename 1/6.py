import numpy as np

NN = 5
j = 1.5 + 0.1 * NN
k = j
l = k - 0.1
m = 1
k = 0
l = 0
A = np.array([[j * m, 0.5 * j, 0, 0.2 * l, 0],
              [0.5 * j, j, 0.3 * j, 0, 0.1 * l],
              [0, 0.3 * j, 10, -0.3 * j, 0.5 * l],
              [0.2 * k, 0, -0.3 * j, j, -0.1 * j],
              [0, 0.1 * k, 0.5 * k, -0.1 * j, j * m]])
print("Matrix A")
print(A)
r = np.array([-j + 0.05 * j * j,
              -0.8 * j + 0.1 * j * j - 0.02 * l * j,
              -10 + 0.03 * j * j - 0.1 * l * j,
              -0.2 * k + 0.3 * j + 0.02 * j * j,
              0.01 * k * j - 0.5 * k - 0.2 * j * j])
print(r)
n = 5

b = np.zeros(n)
c = np.zeros(n)
d = np.zeros(n)

for i in range(0, n):
    for j in range(0, n):
        if A[i][j] != 0:
            if i > j:
                b[j + 1] = A[i][j]
            elif i == j:
                c[j] = A[i][j]
            else:
                d[j - 1] = A[i][j]
print(" b")
print(b)
print(" c")
print(c)
print(" d")
print(d)
x = np.zeros(5)

print("delta")
delta = np.zeros(5)
lyambda = np.zeros(5)

eps = 0.00001

for i in range(n):
    delta[i] = -d[i] / (c[i] + b[i] * delta[i - 1])
    lyambda[i] = (r[i] - b[i] * lyambda[i - 1]) / (c[i] + b[i] * delta[i - 1])

print(delta)
print(lyambda)

x[n - 1] = lyambda[n - 1]

for i in range(n - 2, -1, -1):
    x[i] = delta[i] * x[i + 1] + lyambda[i]

print(f'x = {x}')
print("Ax = r")
print(np.dot(A, x))
