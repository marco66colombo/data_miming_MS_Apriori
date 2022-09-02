# This is a sample Python script.
from config.config import ROOT_DIR

transactions = []

with open(ROOT_DIR + '/files/input_data.txt', 'r') as filestream:
    for line in filestream:
        currentline = line.split(",")
        currentline[-1] = currentline[-1].strip()
        transactions.append(currentline)

f = open(ROOT_DIR + '/files/input_parameters.txt','r')


print(transactions)


#dizionario per contare le occorrenze e poi ciclo sui valori per eliminare quelli sotto al minsup