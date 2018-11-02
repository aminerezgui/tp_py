import math
import cmath
import numpy as np

def f(x):
        return math.exp(-1 * x) - x
def df(x):
        return -1 * math.exp(-1 * x) - 1

def newton1d(f, df,x0, eps, N):
        x = x0
        i = 0
        while abs(f(x)) >  eps and i < N:
                x = x - f(x)/df(x)
                i = i + 1
        if i == N :
                return False
        else :
                return x

def racine(x, n):
        def f(y):
                return y**n - x
        def df(y):
                return n * y**(n - 1)
        return newton1d(f, df, 1.0 , 1.e-10, 1000)

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

def g(x):
	return np.array([np.cos(x[0]) - np.sin(x[1]), np.exp(-1 * x[0]) - np.cos(x[1])])
def dg(x):
	return np.array([[-1 * np.sin(x[0]), -1 * np.cos(x[1])], [-1 * np.exp(-1 * x[0]), np.sin(x[1])]])

def newton(f, df, x0, eps, N):
	x = x0
	i = 0
	while np.linalg.norm(f(x)) > eps and i < N:
		x = x - np.linalg.solve(df(x), f(x))
		i = i + 1
	if i == N:
		return False
	else:
		return x

def racinec(x0, x = 1, n = 3):
        def f(y):
                return y**n - x
        def df(y):
                return n * y**(n - 1)
        return newton1d(f, df, x0 , 1.e-10, 1000)

