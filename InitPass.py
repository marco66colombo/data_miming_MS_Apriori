
def initPass(T, MS):
    I = {}
    for transaction in T:
        for i in transaction:
            if I.get(i) is not None:
                I[i] = I[i] + 1
            else:
                I[i] = 1

    L = I.items()
    return sorted(L, key=lambda a: MS[a[0]] if MS.get(a[0]) is not None else MS['rest']), I


def computeF1(L, MS, n):
    F1 = []
    for l in L:
        mis = MS[l[0]] if MS.get(l[0]) is not None else MS['rest']
        if l[1]/n >= mis:
            F1.append(((l[0],), l[1]))

    return F1
