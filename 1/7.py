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
b = np.array([-j + 0.05 * j * j,
              -0.8 * j + 0.1 * j * j - 0.02 * l * j,
              -10 + 0.03 * j * j - 0.1 * l * j,
              -0.2 * k + 0.3 * j + 0.02 * j * j,
              0.01 * k * j - 0.5 * k - 0.2 * j * j])
print(b)
n = 5

E = np.eye(5)

l = 1 / 2
S = np.linalg.inv(A) * l

B = E - np.dot(S, A)

c = np.dot(S, b)

x0 = np.zeros(5)
x1 = np.dot(B, x0) + c

eps = 0.00001
while True:
    t = x0
    x0 = x1
    x1 = np.dot(B, x0) + c
    if (np.linalg.norm(x1 - x0) < eps):
        break

print(np.linalg.solve(A, b))
print(f'x = {x1}')
