
def initPass(T, MS):
    I = {}
    for transaction in T:
        for i in transaction:
            if I.get(i) is not None:
                I[i] = I[i] + 1
            else:
                I[i] = 1

    L = I.items()
    return sorted(L, key=lambda a: MS[a[0]] if MS.get(a[0]) is not None else MS['rest'])

