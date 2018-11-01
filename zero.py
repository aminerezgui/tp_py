import math


def f(x):
    return math.exp(-1 * x) - x


def secant1d(f, x0, x1, eps = 1.e-10, N = 1000):
    i = 0
    u = x0
    v = x1
    x = x0
    while abs(f(x)) > eps and i < N:
        x = (u * f(v) - v * f(u)) / (f(v) - f(u))
        u = v
        v = x
        i = i +1
    if i == N:
        return false
    else:
        return x

