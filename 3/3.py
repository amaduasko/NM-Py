import sympy as sp

NN = 5
xi = [-3, -2, 0, 2, 3]
yi = [64, 14, 4, 8, 32]

n = len(xi)
x = sp.symbols('x')
N = 0


def f(k, index):
    if k == 1:
        return yi[index]
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
print(N.subs(x, xi[0]))
print(N.subs(x, xi[1]))
print(N.subs(x, xi[2]))
print(N.subs(x, xi[3]))
print(N.subs(x, xi[4]))
