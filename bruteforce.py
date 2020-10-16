

def brute_force(p, t):
    comparisons = 0
    size_p = len(p)
    size_t = len(t)
    for i in range(size_t - size_p + 1):
        window = t[i:i + size_p]
        for j in range(size_p):
            comparisons += 1
            if p[j] == window[j]:
                if j+1 == size_p:
                    return i, comparisons
                continue
            else:
                break
    return -1, comparisons


