

def level2gen(L, phi, n, MS):
    C2 = []
    for i in range(len(L)):
        if l[1][i]/n >= MS[l[0][i]]:
            for j in range(i+1, len(L)):
                if l[1][j] >= MS[l[0][i]] and abs(l[1][j]/n - l[1][i]/n) <= phi:
                    C2.append(((l[0][i], l[0][j]), 0))
    return C2

