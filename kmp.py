# KNUTH-MORRIS-PRATT ALGORITHM

def failure_function(p):
    f = [0] * len(p)
    f[0] = 0
    j = 0
    i = 1
    while i < len(p):
        if p[i] == p[j]:
            f[i] = j+1
            i += 1
            j += 1
        elif j > 0:
            j = f[j-1]
        else:
            f[i] = 0
            i += 1
    return f


def knuth_morris_pratt(t, p):
    f = failure_function(p)
    comparisons = 0
    n = len(t)
    m = len(p)
    i = 0
    j = 0
    while i < n:
        comparisons += 1
        if t[i] == p[j]:
            if j == m - 1:
                return i - j, comparisons
            else:
                i += 1
                j += 1
        else:
            if j > 0:
                j = f[j - 1]
            else:
                i += 1
                j = 0
    return -1, comparisons

