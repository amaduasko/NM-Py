import numpy as np
import math


def me(A):
    max_el = abs(A[0, 1])
    I, J = 0, 1
    for i in range(len(A)):
        for j in range(i + 1, len(A[0])):
            if max_el < abs(A[i, j]):
                max_el = abs(A[i, j])
                I, J = i, j
    return I, J


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
n = len(A)
res = []

eps = 0.0001

while abs(A[me(A)[0], me(A)[1]]) > eps:

    if (A[me(A)[0], me(A)[0]] - A[me(A)[1], me(A)[1]]) == 0:
        alpha = math.pi / 4
    else:
        alpha = math.atan(2 * A[me(A)[0], me(A)[1]] / (A[me(A)[0], me(A)[0]] - A[me(A)[1], me(A)[1]])) / 2
    # print(me(A))
    # print((A[me(A)[0], me(A)[0]], A[me(A)[1], me(A)[1]]))

    Q = np.eye(n)
    Q[me(A)[0], me(A)[0]] = math.cos(alpha)
    Q[me(A)[1], me(A)[1]] = math.cos(alpha)

    Q[me(A)[0], me(A)[1]] = -math.sin(alpha)
    Q[me(A)[1], me(A)[0]] = math.sin(alpha)

    res.append(Q)
    A = np.dot(np.dot(np.transpose(Q), A), Q)

print(np.diagonal(A), "\n")

vector = res[0]

for i in range(1, len(res)):
    vector = np.dot(vector, res[i])

for i in range(n):
    a = vector[i, i]
    for j in range(n):
        vector[j, i] /= a

print(vector)

print(np.linalg.eig(A))
