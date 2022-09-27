# initializes the transactions by sorting their items by increasing values of MIS(item)
from config.config import ROOT_DIR


def sortTransactions(T, MS):
    for i in range(len(T)):
        T[i] = sorted(T[i], key=lambda a: MS[a] if MS.get(a) is not None else MS['rest'])


def parseFile(input_data, input_parameters):
    transactions = []
    MS = {}
    phi = 0.0

    # reads file input data and generates a list of arrays containing the transactions
    with open(ROOT_DIR + '/files/' + input_data, 'r') as filestream:
        for line1 in filestream:
            line = line1.replace(" ","")
            currentline = line.split(",")
            currentline[-1] = currentline[-1].strip()
            #for i in range(len(currentline)): currentline[i] = currentline[i].replace(" ", "")
            transactions.append(currentline)

    # reads file input data and generates a dictionary with pair key-value: x-MIS(x) and puts in var SDC the
    # correspondent value
    with open(ROOT_DIR + '/files/' + input_parameters, 'r') as filestream:
        for line1 in filestream:

            line = line1.replace(" ", "")

            if line.startswith('MIS'):
                first = line.split('(')
                first[-1] = first[-1].strip()
                second = first[1].split(")")
                third = second[1].split("=")

                if second[0].strip() == "rest":
                    MS['rest'] = float(third[1].strip())
                else:
                    MS[second[0]] = float(third[1].strip())

            if line.startswith('SDC'):
                currentline = line.split('=')
                phi = float(currentline[1].strip())

    print(MS);
    #sortTransactions(transactions, MS)
    n = len(transactions)

    return transactions, MS, phi, n
