from random import randint
import math

def random_odd(k):
    r = randint(2**(k - 1), 2**k)
    while(r % 2 == 0):
        r = randint(2**(k - 1), 2**k)
    return r


def isprime(n):
    if n % 2 == 0 and n!= 2:
        return False
    d = 3
    while(d <= math.sqrt(n)):
        if n % d == 0:
            return False
        d = d + 2
    return True


def generate(k, primality):
    r = random_odd(k)
    while(not(primality(r))):
        r = random_odd(k)
    return r


def fermat_test(n):
    for a in range(1, n):
        if (a**(n-1) % n) != 1:
            return False
    return True
