__author__ = "Douglas"

import libplnbsi

def sortTamLst(lst):
    for i in range(len(lst)-1):
        for i in range(len(lst)-1):
            if (len(lst[i]) < len(lst[i+1])):
                aux = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = aux
            #fim if
        #fim for
    #fim for
    return lst
#fim funcao

def extraiPadroes(pTexto, lstPadroes):
    lstPadroes = sortTamLst(lstPadroes)
    lstTokens, lstPos = libplnbsi.tokenizador(pTexto)
    strConfic = libplnbsi.codifica(lstTokens)
    lstPadTexto = []

    print(strConfic)
    print(lstTokens)

    for pd in range(len(lstPadroes)):
        pos = strConfic.find(lstPadroes[pd])
        while(pos != -1):
            strPal = ''
            strConfic = strConfic.replace(lstPadroes[pd], "*" * len(lstPadroes[pd]), 1)
            for el in range(len(lstPadroes[pd])):
                strPal += lstTokens[pos + el] + " "
            #fim for
            if (strPal):
                lstPadTexto.append(strPal)
            #fim if
            pos = strConfic.find(lstPadroes[pd])
        #fim while
    #fim for
    print(strConfic)
    return lstPadTexto
#fim funcao

def main():
    padroes = ['MMpMM', 'MMpM', 'MpM', 'MMM', 'MM', 'M', 'N/N/N']

    arq = open('arqOrigMan/constituicaoBr.txt', 'rt')
    # lstTokens = ['Semana', 'passada', '(', '22', '/', '12', '/', '2014', ')', 'eu', 'toquei', 'no', 'assunto', 'do', 'módulo', 'Progress', ',', 'destinado', 'a', 'levar', 'suprimentos', 'para', 'a', 'Estação', 'Espacial', 'Internacional', ',', 'ISS', 'em', 'inglês', ',', 'que', 'falhou', 'assim', 'que', 'foi', 'colocada', 'em', 'órbita', '.', 'Mas', 'relembrando', 'os', 'fatos', ',', 'foi', 'assim', '.']

    libplnbsi.geraTabFreq(extraiPadroes(arq.read(), padroes))
    # libplnbsi.geraTabFreq(lstTokens)

    return 0
#fim main

if __name__ == '__main__':
    main()
#fim if
