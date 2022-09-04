# This is a sample Python script.
from config.config import ROOT_DIR

transactions = []
SDC = 0.0
MIS = {}

with open(ROOT_DIR + '/files/input_data.txt', 'r') as filestream:
    for line in filestream:
        currentline = line.split(",")
        currentline[-1] = currentline[-1].strip()
        transactions.append(currentline)

with open(ROOT_DIR + '/files/input_parameters.txt', 'r') as filestream:

    for line in filestream:

        if line.startswith('MIS'):
            first = line.split('(')
            first[-1] = first[-1].strip()
            second = first[1].split(")")
            third = second[1].split("=")

            if second[0] == "rest":
                MIS['rest'] = float(third[1])
            else:
                MIS[second[0]] = float(third[1])

        if line.startswith('SDC'):
            currentline = line.split('=')
            SDC = float(currentline[1])

    print(transactions)
    print(SDC)
    print(MIS)

# def sort(transaction, sorting):
#     transaction = sorted(transaction, sorting)
# def init(transactions):
#     for transaction in transactions:
#         sort(transaction, lambda i : {MIS[i] if MIS.get(i) is not None else MIS['rest']})

# init(transactions)
# print(transactions)









#dizionario per contare le occorrenze e poi ciclo sui valori per eliminare quelli sotto al minsup
