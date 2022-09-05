

def printOutput(F):
    for i in range(len(F)):
        print('(Length-' + str(i+1) + " " + str(len(F[i])))
        for elem in F[i]:
            string = str(elem[0]).replace('\'', '').replace(',', '')
            print(string)
        print(')')
