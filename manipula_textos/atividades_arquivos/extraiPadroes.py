__author__ = "Douglas"

import libplnbsi

def main():
    padroes = ['MMpMM', 'MMpM', 'MpM', 'MMM', 'MM', 'M', 'N/N/N']

    nomeArqLtr = 'arqOrigMan/codigocivilbr.txt'
    nomeArqEsc = 'arqDestMan/tabFreqCodigocivilbr.csv'
    # nomeArqLtr = 'arqOrigMan/codigoTransitoBr1997.txt'
    # nomeArqEsc = 'arqDestMan/tabFreqCodigoTransitoBr1997.csv'
    # nomeArqLtr = 'arqOrigMan/constituicaoBr.txt'
    # nomeArqEsc = 'arqDestMan/tabFreqConstituicaoBr.csv'
    # nomeArqLtr = 'arqOrigMan/bibliacatnt.txt'
    # nomeArqEsc = 'arqDestMan/tabFreqBibliacatnt.csv'
    # nomeArqLtr = 'arqOrigMan/bibliacatvt.txt'
    # nomeArqEsc = 'arqDestMan/tabFreqBibliacatvt.csv'

    arqCont = open(nomeArqLtr, 'rt')

    texto = arqCont.read()
    # lstTokens = ['Semana', 'passada', '(', '22', '/', '12', '/', '2014', ')', 'eu', 'toquei', 'no', 'assunto', 'do', 'módulo', 'Progress', ',', 'destinado', 'a', 'levar', 'suprimentos', 'para', 'a', 'Estação', 'Espacial', 'Internacional', ',', 'ISS', 'em', 'inglês', ',', 'que', 'falhou', 'assim', 'que', 'foi', 'colocada', 'em', 'órbita', '.', 'Mas', 'relembrando', 'os', 'fatos', ',', 'foi', 'assim', '.']

    #
    libplnbsi.geraTabFreq(libplnbsi.extraiPadroes(texto, padroes), nomeArqEsc)
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
