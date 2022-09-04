# This is a sample Python script.
from InitPass import *
from Parse import *

def main():
    F = []
    transactions, MS, phi, n = parseFile()
    L = initPass(transactions, MS)
    F.append(computeF1(L, MS, n))

    print('n =', n)
    print('transactions =', transactions)
    print('phi =', phi)
    print('L =', L)
    print('F =', F)


if __name__ == '__main__':
    main()
