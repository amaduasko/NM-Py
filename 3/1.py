import sympy as sp

NN = 5
xi = [-3, -2, 0, 2, 3]
yi = [64, 14, 4, 8, 32]
n = len(xi)
x = sp.symbols('x')
L = 0


def w(index):
    ww = 1
    for g in range(n):
        if g != index:
            ww *= x - xi[g]
    return ww


for i in range(n):
    L += yi[i] * w(i) / (w(i).subs(x, xi[i]))

print(sp.simplify(L))
print(L.subs(x, xi[0]))
print(L.subs(x, xi[1]))
print(L.subs(x, xi[2]))
print(L.subs(x, xi[3]))
print(L.subs(x, xi[4]))
