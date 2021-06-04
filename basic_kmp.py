def matching_KMP(t, p, pnext):
    n = len(t)
    m = len(p)
    i = j = 0
    while j < n and i < m:
        if i == -1 or t[j] == p[i]:
            j += 1
            i += 1
        else:
            i = pnext[i]
    if i == m:
        # matching
        return j - 1
    return -1    # failed


def get_pnext(p):
    k = -1
    i = 0
    m = len(p)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i += 1
            k += 1
            pnext[i] = k
        else:
            k = pnext[k]
    return pnext
