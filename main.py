# This is a sample Python script.
from config.config import ROOT_DIR

transactions = []
SDC = 0.0
MIS = {}

# reads file input data and generates a list of arrays containing the transactions
with open(ROOT_DIR + '/files/input_data.txt', 'r') as filestream:
    for line in filestream:
        currentline = line.split(",")
        currentline[-1] = currentline[-1].strip()
        for i in range(len(currentline)): currentline[i] = currentline[i].replace(" ", "")
        transactions.append(currentline)

# reads file input data and generates a dictionary with pair key-value: x-MIS(x) and puts in var SDC the
# correspondent value
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


# initializes the transactions by sorting their items by increasing values of MIS(item)
def init(x):
    for i in range(len(x)):
        x[i] = sorted(x[i], key=lambda a: MIS[a] if MIS.get(a) is not None else MIS['rest'])


print(MIS)
print(MIS['rest'])
init(transactions)
print(transactions)

# dizionario per contare le occorrenze e poi ciclo sui valori per eliminare quelli sotto al minsup
