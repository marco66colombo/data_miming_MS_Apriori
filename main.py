# This is a sample Python script.
from InitPass import *
from Parse import *
from config.config import ROOT_DIR


def main():
    F = []
    transactions, MS, phi, n = parseFile()
    L = initPass(transactions, MS)
    F.append(computeF1(L, MS, n))

    print(n)
    print(transactions)
    print(phi)
    print(L)
    print(F)
    print(F[0][0][0][0])


if __name__ == '__main__':
    main()
