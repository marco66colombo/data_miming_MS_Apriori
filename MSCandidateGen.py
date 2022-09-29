import itertools


def checkSubset(C, c, k, MS):
    # populate S
    S = list(itertools.combinations(c, k - 1))

    for s in S:
        mis0 = MS[c[0]] if MS.get(c[0]) is not None else MS['rest']
        mis1 = MS[c[1]] if MS.get(c[1]) is not None else MS['rest']
        if c[0] in s or mis0 == mis1:
            if not (set(s).issubset(c)):
                return

    C.append((c, 0))
    return


def msCandidateGen(F, k, phi, MS, L_map, n):
    C = []
    i = 0

    while i < len(F):
        newtuple = F[i][0][:(k-1)]
        start = i
        i += 1

        while i != len(F) and newtuple == F[i][0][:(k-1)]:
            i += 1

        end = i

        for j in range(start, end):
            for h in range(j+1, end):
                sup1 = L_map[F[j][0][k-1]] / n
                sup2 = L_map[F[h][0][k-1]] / n

                if abs(sup1 - sup2) <= phi:
                    tuple_one_element = (F[j][0][k-1],)
                    tuple_two_element = (F[h][0][k-1],)
                    checkSubset(C, (newtuple + tuple_one_element + tuple_two_element), k, MS)
                    #C.append((newtuple + tuple_one_element + tuple_two_element))

    return C
