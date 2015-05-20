__author__ = 'douglas'

import libplnbsi

def higherFreq(lstFreq):
    return lstFreq[0]
# fim funcao

def printHigherFreq(tupFreq):
    print("Maior frequencia: %s - %s vez(es)\n" %(tupFreq[0], tupFreq[1]))
# fim funcao

def lowFreq(lstFreq):
    return lstFreq[-1]
# fim funcao

def printLowFreq(tupFreq):
    print("Menor frequencia: %s - %s vez(es)\n\n" %(tupFreq[0], tupFreq[1]))
# fim funcao

def main():
    libplnbsi.leituraSena('arqDestMan/arqFregSena.txt', 'arqOrigMan/arqDezenasMega.txt', '\t')
    lstFreqSena = libplnbsi.leituraFregSena('arqDestMan/arqFregSena.txt', ',', [0, 1])

    printHigherFreq(higherFreq(lstFreqSena))
    printLowFreq(lowFreq(lstFreqSena))
# fim main

main()