import numpy as np


a = {1:{2, 5} , 2:{1, 5, 3}, 3:{2, 4}, 4:{5, 6}, 5:{4, 1, 2}, 6:{4}}
b = {1: set([2, 3, 4, 5]), 2: set([1, 3, 4, 5]), 3: set([1, 2, 4, 5]), 4: set([1, 2, 3, 5]), 5: set([1, 2, 3, 4])}
c = {1:{2, 5, 6}, 2:{1, 3, 7},3:{2, 4, 8},4:{3, 5, 9},5:{1, 4, 10}, 6:{1, 8, 9}, 7:{2, 9, 10}, 8:{3, 6, 10}, 9:{4, 7, 6}, 10:{5, 7, 8}}

def complet(n):
	d = {}
	i = 1
	while i < n or i == n:
		d[i] = set()
		k = 1
		while k < n or k == n:
			if k != i:
				d[i].add(k)
			k = k + 1
		i = i + 1
	return d


def corriger(g):
	d = g.copy()
	for i in g:
		for k in g[i]:
			if not(k in g):
				if k in d:
					d[k].add(i)
				else :
					d[k] = set()
					d[k].add(i)
	return d


def aretes(g):
	a = set()
	for i in g:
		for k in g[i]:
			if not((k,i) in a):
				a.add((i, k))
	return a


def triangles(g):
	e = set()
	for i in g:
		for j in g[i]:
			for k in g[j]:
				if k in g[i]:
					l = [i, j, k]
					l.sort()
					t = tuple(l)
					if not(t in e):
						e.add(t)
	return e

def matadja(g):
	n = len(g)
	m = np.zeros((n,n), dtype = int)
	for a in aretes(g):
		m[a[0] - 1][a[1] - 1] = 1
		m[a[1] - 1][a[0] - 1] = 1
	return m


def graphe(m):
	g = {}
	n = np.shape(m)[0]
	for i in range(1, n+1):
		g[i] = set()
	for i in range(n):
		for k in  range(n):
			if m[i][k] == 1:
				g[i + 1].add(k + 1)
	return g

