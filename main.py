# This is a sample Python script.
from InitPass import *
from Parse import *
from Level2CandidateGen import *
from MSCandidateGen import *
from PrintOut import printOutput


def main():
    F = []
    C = []
    transactions, MS, phi, n = parseFile()
    L, L_map = initPass(transactions, MS)
    F.append(computeF1(L, MS, n))

    k = 2
    while len(F[k-2]) != 0:
        if k == 2:
             C.append(level2CandidateGen(L, phi, n, MS))
        else:
             C.append(msCandidateGen(F[k-2], k-1, phi, MS, L_map, n))

        for t in transactions:
            for z in range(len(C[k-2])):
                if set(C[k-2][z][0]).issubset(t):
                    C[k-2][z] = (C[k-2][z][0], C[k-2][z][1] + 1)
        F.append([])
        for c in C[k-2]:
            if c[1]/n >= (MS[c[0][0]] if MS.get(c[0][0]) is not None else MS['rest']):
                F[k-1].append(c)

        k += 1

    F.pop()

    printOutput(F);
    print('Final F is', F)


if __name__ == '__main__':
    main()
