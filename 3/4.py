import sympy as sp
import math

NN = 5
xi = [0, math.pi / 6, math.pi / 4, math.pi / 3]
n = len(xi)
x = sp.symbols('x')
N = 0


def f(k, index):
    if k == 1:
        return math.tan(xi[index])
    return (f(k - 1, index + 1) - f(k - 1, index)) / (xi[index + k - 1] - xi[index])


def multi(index):
    s = 1
    for j in range(index):
        s *= (x - xi[j])
    return s


for i in range(1, n + 1):
    print("i=", i, " ", f(i, 0))
    N += f(i, 0) * multi(i - 1)
print("N = ", N)
for i in range(n):
    print("N(i) ", N.subs(x, xi[i]))

print("y")
print(f(1, 0), f(1, 1), f(1, 2), f(1, 3))
