# This is a sample Python script.
from InitPass import *
from Parse import *
from Level2CandidateGen import *
from MSCandidateGen import *

def main():
    F = []
    C = []
    transactions, MS, phi, n = parseFile()
    L, L_map = initPass(transactions, MS)
    F.append(computeF1(L, MS, n))

    print('n =', n)
    print('transactions =', transactions)
    print('phi =', phi)
    print('L =', L)
    print('F =', F)

    k = 2
    # while len(F[k-2]) != 0:
    #     if k == 2:
    #         C[0] = level2gen(L, phi, n, MS)
    #     else:
    #         C[k-2] = msCandidateGen(F, k, phi, MS, L_map, n)

    print(level2CandidateGen(L, phi, n, MS))



if __name__ == '__main__':
    main()
