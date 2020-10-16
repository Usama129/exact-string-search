# RABIN-KARP ALGORITHM

from timeit import default_timer as timer


def rabin_karp(t, p):
    comparisons = 0
    m = len(p)
    n = len(t)
    q = larger_prime(m)
    c = pow(10, m-1) % q
    fp = 0
    ft = 0

    for i in range(m):
        fp = (10*fp + ord(p[i])) % q
        ft = (10*ft + ord(t[i])) % q

    for s in range(n - m + 1):
        if fp == ft:
            for j in range(m):
                comparisons += 1
                if p[j] == t[s+j]:
                    if j == m - 1:
                        return s, comparisons
                else:
                    break
        if s >= n-m:
            return -1, comparisons
        ft = ((ft - c * ord(t[s])) * 10 + ord(t[s+m])) % q

    return -1, comparisons


def larger_prime(m):
    n = m+1
    while True:
        if is_prime(n):
            return n
        n += 1


def is_prime(n):
    if n > 1:
        if n % 2 == 0:
            return False
        for i in range(2, n):
            if (n % i) == 0:
                return False
        else:
            return True

    else:
        return False

