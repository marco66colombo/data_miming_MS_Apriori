
def initPass(T, MS, n):
    I = {}
    L = []
    for transaction in T:
        for i in transaction:
            if I.get(i) is not None:
                I[i] = I[i] + 1
            else:
                I[i] = 1

    L_pre = sorted(I.items(), key=lambda a: MS[a[0]] if MS.get(a[0]) is not None else MS['rest'])

    i = 0
    mis_i = (MS[L_pre[i][0]] if MS.get(L_pre[i][0]) is not None else MS['rest'])

    while i < len(L_pre) and L_pre[i][1]/n < mis_i:
        i += 1
        mis_i = (MS[L_pre[i][0]] if MS.get(L_pre[i][0]) is not None else MS['rest'])

    L.append(L_pre[i])

    for j in range(i+1, len(L_pre)):
        if L_pre[j][1]/n >= mis_i:
            L.append(L_pre[j])

    return L, I


def computeF1(L, MS, n):
    F1 = []
    for l in L:
        mis = MS[l[0]] if MS.get(l[0]) is not None else MS['rest']
        if l[1]/n >= mis:
            F1.append(((l[0],), l[1]))

        #print('elem: '+str(l[0])+' mis = ' + str(mis) + ' real sup: ' + str(l[1]/n) )

    return F1
