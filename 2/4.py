import math

NN = 5


def f(x):
    return math.exp(-x) - x - 2


def f1(x):
    return -math.exp(-x) - 1


def f2(x):
    return math.exp(-x)


a, b = -3, 0

eps = 0.001


def comb(first_element, second_element):
    xn = first_element
    xn1 = xn - f(xn) / (f(second_element) - f(xn)) * (second_element - xn)
    xn_ = second_element
    xn1_ = xn_ - f(xn_) / f1(xn_)
    while abs(xn1 - xn1_) > eps:
        xn = xn1
        xn1 = xn - f(xn) / (f(second_element) - f(xn)) * (second_element - xn)
        xn_ = xn1_
        xn1_ = xn_ - f(xn_) / f1(xn_)
    return xn1


print(f'comb(a, b) = {comb(a, b)}', '\n')
print(f'f(comb(a, b)) = {f(comb(a, b))}', '\n')
