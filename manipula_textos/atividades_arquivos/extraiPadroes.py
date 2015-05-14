__author__ = "Douglas"

import libplnbsi

def main():
    padroes = ['MMpMM', 'MMpM', 'MpM', 'MMM', 'MM', 'M', 'N/N/N']

    # arqCont = open('arqOrigMan/codigocivilbr.txt', 'rt')
    # arqCont = open('arqOrigMan/codigoTransitoBr1997.txt', 'rt')
    arqCont = open('arqOrigMan/constituicaoBr.txt', 'rt')
    # arqCont = open('arqOrigMan/bibliacatnt.txt', 'rt')
    # arqCont = open('arqOrigMan/bibliacatvt.txt', 'rt')

    texto = arqCont.read()
    # lstTokens = ['Semana', 'passada', '(', '22', '/', '12', '/', '2014', ')', 'eu', 'toquei', 'no', 'assunto', 'do', 'módulo', 'Progress', ',', 'destinado', 'a', 'levar', 'suprimentos', 'para', 'a', 'Estação', 'Espacial', 'Internacional', ',', 'ISS', 'em', 'inglês', ',', 'que', 'falhou', 'assim', 'que', 'foi', 'colocada', 'em', 'órbita', '.', 'Mas', 'relembrando', 'os', 'fatos', ',', 'foi', 'assim', '.']

    #
    libplnbsi.geraTabFreq(libplnbsi.extraiPadroes(texto, padroes))
    # lstTeste, lstPos = libplnbsi.tokenizador(texto)
    # strCodifica = libplnbsi.codifica(lstTeste)
    #
    # lstSep = libplnbsi.atualizaSeparadores(texto)
    #
    # print(strCodifica)
    #
    # for el in strCodifica:
    #     if el not in lstSep and el not in ['M', 'm', 'N', 'a', 'c', 'p']:
    #         print(el)
        #fim if
    #fim for

    arqCont.close()
    return 0
#fim main

if __name__ == '__main__':
    main()
#fim if
