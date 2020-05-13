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

y = np.zeros(6)
y[5] = 1
Ab = np.column_stack((A, -b))
Ab1 = np.row_stack((Ab, y))
print(Ab1)

u = np.zeros((n + 1, n + 1))
v = np.zeros((n + 1, n + 1))

u[0] = Ab1[0]
v[0] = u[0] / np.linalg.norm(u[0])

for j in range(1, n + 1):
    u[j] = Ab1[j] - sum(np.dot(Ab1[j], v[i]) * v[i] for i in range(0, j))
    v[j] = u[j] / np.linalg.norm(u[j])

print('y')
print(u[5][:5] / u[5][5])
y = np.zeros(n)
for i in range(n):
    y[i] = u[5][i] / u[5][5]

print("y")
print(y)
print("Ay = b")
print(np.dot(A, y))
