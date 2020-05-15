import sympy as sp
import numpy as np

NN = 5
X = [-3, -2, 0, 2, 3]
Y = [64, 14, 4, 8, 32]
n = len(X)
x = sp.symbols('x')


def prob(A, r):
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
    xx = np.zeros(5)

    print("delta")
    delta = np.zeros(5)
    lyambda = np.zeros(5)

    for i in range(n):
        delta[i] = -d[i] / (c[i] + b[i] * delta[i - 1])
        lyambda[i] = (r[i] - b[i] * lyambda[i - 1]) / (c[i] + b[i] * delta[i - 1])

    print(delta)
    print(lyambda)

    xx[n - 1] = lyambda[n - 1]

    for i in range(n - 2, -1, -1):
        xx[i] = delta[i] * xx[i + 1] + lyambda[i]

    print("xx")
    print(xx)
    print("Ax = r")
    print(np.dot(A, xx))

    return xx


h = np.zeros(n - 1)
for i in range(n - 1):
    h[i] = X[i + 1] - X[i]
print("h", h)
A = np.array([[1, 0, 0, 0, 0],
              [1 / 6 * h[0], 1 / 3 * (h[0] + h[1]), 1 / 6 * h[1], 0, 0],
              [0, 1 / 6 * h[1], 1 / 3 * (h[1] + h[2]), 1 / 6 * h[2], 0],
              [0, 0, 1 / 6 * h[2], 1 / 3 * (h[2] + h[3]), 1 / 6 * h[3]],
              [0, 0, 0, 0, 1]])
b = np.zeros(n)
for i in range(1, n - 1):
    for j in range(1, n - 1):
        '''
    if ():
      A[i][j] = 0
    else:
      A[i][j]=1/6*h[i]*M[i-1] + 1/3*(h[i-1]+h[i])*M[i] + 1/6*h[i]*M[i+1]])'''
    b[i] = (Y[i + 1] - Y[i]) / h[i] - (Y[i] - Y[i - 1]) / h[i - 1]
m = np.linalg.solve(A, b)
print(m)


def S3(index):
    return -m[index] / (6 * h[index]) * (x - X[index + 1]) ** 3 + m[index + 1] / (6 * h[index]) * (x - X[index]) ** 3 + (
            (Y[index + 1] - Y[index]) / h[index] - h[index] / 6 * (m[index + 1] - m[index])) * (x - X[index]) + Y[index] - m[index] / 6 * (h[index]) ** 2


print(sp.expand(S3(0)), "\n")
print(sp.expand(S3(1)), "\n")
print(sp.expand(S3(2)), "\n")
print(sp.expand(S3(3)), "\n")
