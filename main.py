# This is a sample Python script.
from InitPass import *
from Parse import *
from Level2CandidateGen import *
from MSCandidateGen import *
from PrintOut import *
import sys


def main():
    F = []
    C = []
    #C.append([])
    transactions, MS, phi, n = parseFile(sys.argv[1], sys.argv[2])
    set_transactions = []
    #create a list of sets for efficiency purposes
    for t in transactions:
        set_transactions.append(set(t))

    print('Input file parsing completed.')
    L, L_map = initPass(transactions, MS, n)
    print('initPass completed.')
    F.append(computeF1(L, MS, n))

    k = 2

    while len(F[k-2]) != 0:

        print('Current value of k in the cycle: ' + str(k))

        if k == 2:
             C.append(level2CandidateGen(L, phi, n, MS))
        else:
             C.append(msCandidateGen(F[k-2], k-1, phi, MS, L_map, n))

        print('Candidate generation completed.')

        for t in set_transactions:
            for z in range(len(C[0])):
                #if set(C[k-2][z][0]).issubset(t):
                flag = True
                for elem in (C[0][z][0]):
                    if not (elem in t):
                        flag = False
                if flag:
                    C[0][z] = (C[0][z][0], C[0][z][1] + 1)
        F.append([])

        print('Compute count of the itemsets completed.')

        for c in C[0]:
            if c[1]/n >= (MS[c[0][0]] if MS.get(c[0][0]) is not None else MS['rest']):
                F[k-1].append(c)

        C.pop()
        k += 1

    F.pop()

    printOutput(F, sys.argv[3])
    printOutputTerminal(F)


if __name__ == '__main__':
    main()
