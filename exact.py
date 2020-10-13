

def brute_force(p, t):
    pos = []
    comparisons = 0
    sizeP = len(p)
    sizeT = len(t)
    i = 0
    for i in range(sizeT-sizeP+1):
        if t[i:i+sizeP] == p:
            pos.append(i)
        comparisons += sizeP
    return pos, comparisons

