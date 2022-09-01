# This is a sample Python script.
from config.config import ROOT_DIR


f = open(ROOT_DIR + '/files/input_data.txt', 'r')

print(f.readline())