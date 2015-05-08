__author__ = "Douglas"

import libplnbsi

def extraiPadroes(pTexto):
    lstPadroes = ['M', 'MM', 'MpM', 'MMpMM', 'N/N/N', 'MMpM', 'MMM']
    strSep = [' ', '.', ',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '\\', '|', '/', '\n', '\t', '"']
    lstTokens, lstPosicoes = [], []
    strPadroes, pos = '', 0

    lstTokens, lstPos = libplnbsi.tokenizador(pTexto)

    while pos < len(pTexto):
        if (pTexto[pos] not in strSep):
            strBuffer += pTexto[pos]
        else:
            if (strBuffer != ''):
                lstTokens.append(strBuffer)
                lstPosicoes.append(pos-len(strBuffer))
                strBuffer = ''
            #fim if

            if (pTexto[pos] not in [' ', '\t']):
                lstTokens.append(pTexto[pos])
                lstPosicoes.append(pos)
            #fim if
        #fim else
        pos += 1
    #fim while

    if strBuffer != '':
        lstTokens.append(strBuffer)
        lstPosicoes.append(pos-len(strBuffer))
    #fim if


    print(lstTokens)
    print(lstPos)
#fim funcao

def main():
    texto = "Semana passada (22/12/2014) eu toquei no assunto do módulo Progress, destinado a levar suprimentos para a Estação Espacial Internacional, ISS em inglês, que falhou assim que foi colocada em órbita. Mas relembrando os fatos, foi assim."
    lstTokens = ['Semana', 'passada', '(', '22', '/', '12', '/', '2014', ')', 'eu', 'toquei', 'no', 'assunto', 'do', 'módulo', 'Progress', ',', 'destinado', 'a', 'levar', 'suprimentos', 'para', 'a', 'Estação', 'Espacial', 'Internacional', ',', 'ISS', 'em', 'inglês', ',', 'que', 'falhou', 'assim', 'que', 'foi', 'colocada', 'em', 'órbita', '.', 'Mas', 'relembrando', 'os', 'fatos', ',', 'foi', 'assim', '.']

    extraiPadroes(texto)

    return 0
#fim main

if __name__ == '__main__':
    main()
#fim if
