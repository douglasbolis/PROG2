__author__ = 'douglas'

import libplnbsi
from operator import itemgetter

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
# -----------------------------------------------------------------------------------------------

def duplaFregSena(lstDupĺas, linha, sep):
    lstSortSena = [int(s) for s in linha.strip().split(sep)]

    for i in range(len(lstSortSena)-1):
        j = i + 1

        while j < len(lstSortSena):
            lstDupĺas.append(tuple(sorted([lstSortSena[i], lstSortSena[j]])))
            j += 1
        # fim while
    # fim for
# fim funcao

def triplaFregSena(lstTriplas, linha, sep):
    lstSortSena = [int(s) for s in linha.strip().split(sep)]

    for i in range(len(lstSortSena)-2):
        j = i + 1
        while j < (len(lstSortSena)-1):
            k = j + 1
            while k < len(lstSortSena):
                lstTriplas.append(tuple(sorted([lstSortSena[i], lstSortSena[j], lstSortSena[k]])))
                k += 1
            # fim while
            j += 1
        # fim while
    # fim for
# fim funcao

def readDezSortSena(arqOrig, sep):
    lstDuplasSortSena = []
    lstTriplasSortSena = []
    arqSena = open(arqOrig, 'rt')

    linha = arqSena.readline()
    while linha != '':
        duplaFregSena(lstDuplasSortSena, linha, sep)
        triplaFregSena(lstTriplasSortSena, linha, sep)
        linha = arqSena.readline()
    # fim while

    arqSena.close()
    return lstDuplasSortSena, lstTriplasSortSena
# fim funcao

def freqDuplasSortSena(lstDuplas, arqDest):
    dicDuplas = {}

    for dup in lstDuplas:
        if dup in dicDuplas:
            dicDuplas[dup] += 1
        else:
            dicDuplas[dup] = 1
            # fim else
    # fim for

    lstDuplasOrden = sorted(dicDuplas.items(), key=itemgetter(1), reverse=True)

    arqDuplas = open(arqDest, 'wt')
    for el in lstDuplasOrden:
        arqDuplas.write(str(el[0]) + ',' + str(el[1]) + '\n')
    # fim for
    arqDuplas.close()
#fim funcao
# -----------------------------------------------------------------------------------------------

def main():

    lstDuplasSortSena, lstTriplasSortSena = readDezSortSena('arqOrigMan/arqDezenasMega.txt', '\t')
    freqDuplasSortSena(lstDuplasSortSena, 'arqDestMan/arqDuplasSena.txt')
    freqDuplasSortSena(lstTriplasSortSena, 'arqDestMan/arqTriplasSena.txt')
    # libplnbsi.leituraSena('arqOrigMan/arqDezenasMega.txt', 'arqDestMan/arqFregSena.txt', '\t')
    # lstFreqSena = libplnbsi.leituraFregSena('arqDestMan/arqFregSena.txt', ',', [0, 1])

    # printHigherFreq(higherFreq(lstFreqSena))
    # printLowFreq(lowFreq(lstFreqSena))
# fim main

main()