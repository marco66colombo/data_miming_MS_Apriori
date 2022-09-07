

def level2CandidateGen(L, phi, n, MS):
    C2 = []

    for i in range(len(L)):
        mis = MS[L[i][0]] if MS.get(L[i][0]) is not None else MS['rest']

        if L[i][1]/n >= mis:
            for j in range(i+1, len(L)):
                if L[j][1]/n >= mis and abs(L[j][1]/n - L[i][1]/n) <= phi:
                    C2.append(((L[i][0], L[j][0]), 0))
    return C2

