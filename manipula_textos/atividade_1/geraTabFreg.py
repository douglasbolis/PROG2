__author__ = 'douglas'

import libplnbsi

def tabFreg(pTexto, srtSep):
    lst = libplnbsi.separaPalavras(pTexto, srtSep)
    geraTabFreg(lst)
#fim funcao

def geraTabFreg(lstText):
    dic = {}

    for elem in lstText:
        if elem in dic:
            dic[elem] += 1
        else:
            dic[elem] = 1
        #fim else
    #fim for

    for elem in dic:
        print("%s %d" %(elem, dic[elem]))
    #fim for
#fim funcao


def main():
    texto = open('concat_1.txt', 'rt')
    strSep = " "
    tabFreg(texto.read(), strSep)
#fim main

main()