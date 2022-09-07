from config.config import ROOT_DIR


def printOutput(F, output_file):
    f_out = open(ROOT_DIR + '/files/' + output_file, 'w')

    for i in range(len(F)):
        f_out.write('(Length-' + str(i+1) + " " + str(len(F[i])))
        for elem in F[i]:
            string = str(elem[0]).replace('\'', '').replace(',', '')
            f_out.write(string)
        f_out.write(')')

    f_out.close()


def printOutputTerminal(F):

    for i in range(len(F)):
        print('(Length-' + str(i+1) + " " + str(len(F[i])))
        for elem in F[i]:
            string = str(elem[0]).replace('\'', '').replace(',', '')
            print(string)
        print(')')
