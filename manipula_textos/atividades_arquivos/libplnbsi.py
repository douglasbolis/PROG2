__author__ = 'douglas'


"""     FUNÇÕES DE MANIPULAÇÃO DE TEXTOS    """

from operator import itemgetter

#   separaPalavras(...) pega um texto e retorna suas palavras em uma lista
def separaPalavras(pTexto, strSep):
    auxSep = ''
    palSep = []

    for i in pTexto:
        if i not in strSep:
            auxSep += i
        elif auxSep:
            palSep.append(auxSep)
            auxSep = ''
        #fim else
    #fim for

    return palSep
#fim funcao

#   corrente(...) pega um texto e retorna a palavra que esta na posição passada pelo parâmentro
def corrente(pTexto, ppos, strSep):

    if (pTexto[ppos] in strSep):
        return None
    else:
        i = ppos
        while (i >= 0) and (pTexto[i] not in strSep):
            i -= 1
        #fim while
        j = ppos
        while (j < len(pTexto)) and (pTexto[j] not in strSep):
            j += 1
        #fim while
        return pTexto[i+1:j]
    #fim else
#fim funcao

#   anterior(...) pega um texto e retorna a palavra anterior que esta na posição passada pelo parâmentro
def anterior(pTexto, ppos, strSep):
    i = ppos

    if (pTexto[i] not in strSep):
        while (i >= 0) and (pTexto[i] not in strSep):
            i -= 1
        #fim while
    while (i >= 0) and (pTexto[i] in strSep):
        i -= 1
    #fim while

    if i < 0:
        return None
    else:
        return corrente(pTexto, i, strSep)
    #fim else
#fim funcao

#   proxima(...) pega um texto e retorna a próxima palavra que esta na posição passada pelo parâmentro
def proxima(pTexto, ppos, strSep):
    i = ppos

    if (pTexto[i] not in strSep):
        while (i < len(pTexto)) and (pTexto[i] not in strSep):
            i += 1
            #fim while
    while (i < len(pTexto)) and (pTexto[i] in strSep):
        i += 1
    #fim while

    if i < 0:
        return None
    else:
        return corrente(pTexto, i, strSep)
#fim funcao

#   tabFreq(...) transforma o texto em uma lista e chama geraTabFreq(...)
def tabFreq(pTexto, srtSep):
    lst = separaPalavras(pTexto, srtSep)
    geraTabFreq(lst)
#fim funcao

#   geratabFreq(...) imprime a tabela de frequencia da lista passada por parâmetro
def geraTabFreq(lstText):
    dic = {}

    for elem in lstText:
        if elem in dic:
            dic[elem] += 1
        else:
            dic[elem] = 1
        #fim else
    #fim for

    dic = sorted(dic.items(), key=itemgetter(1), reverse=True)

    for elem in dic:
        print("%50s %d" %(elem[0], elem[1]))
    #fim for
#fim funcao

#   insereEspaco(...) retorna o texto passado como parâmetro acrescido de espaços antes e depois de seus separadores
def insereEspaco(pTexto):
    textReturn = ''
    el = 0

    while el < len(pTexto):
        if pTexto[el].isdigit() and ((el+1) < len(pTexto)) and (pTexto[el+1]).isalpha():
            textReturn += pTexto[el] + " "
        elif pTexto[el].isalnum():
            textReturn += pTexto[el]
        else:
            textReturn += " " + pTexto[el] + " "
        #fim else
        el += 1
    #fim for
    return textReturn
#fim funcao

#   insereEspaco(...) retorna o texto passado como parâmetro acrescido de espaços antes e depois de seus separadores
def verificaSeparadores(pTexto):
    arqSep = open('arqDestMan/separadores.txt', 'wt')
    strSep = ' \n\t\n'

    for el in pTexto:
        if not el.isalnum() and el not in strSep:
            strSep += el + '\n'
        #fim if
    #fim for
    arqSep.write(strSep)
    arqSep.close()
#fim funcao

def atualizaSeparadores(pTexto):
    lstSep = []

    verificaSeparadores(pTexto)

    arqSep = open('arqDestMan/separadores.txt', 'rt')
    linha = arqSep.readline()

    while linha != '':
        if linha not in lstSep:
            lstSep.append(linha[:-1])
        #fim if
        linha = arqSep.readline()
    #fim while
    arqSep.close()

    return lstSep
#fim funcao

#   tokenizador(...) retorna uma lista contendo as 'palavras e pontuações' contidas no texto e uma lista de suas posições posições
def tokenizador(pTexto):
    lstSep, lstTokens, lstPosicoes = [], [], []
    strBuffer, pos = '', 0

    lstSep = atualizaSeparadores(pTexto)
    # lstSep = [' ', '\t', '.', ',', '-', ':', ';', ')', '§', '(', '%', '°', '´']
    print(lstSep)
    print(len(lstSep))

    while pos < len(pTexto):
        if (pTexto[pos] not in lstSep):
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

    return lstTokens, lstPosicoes
#fim funcao

#   codifica(...) retorna uma string codificada em alguns codigos como: MmpcaN
def codifica(pLst):
    lstArtigos = ['a', 'as', 'o', 'os', 'um', 'uma', 'umas', 'uns']
    lstConj = ['e', 'nem', 'mas', 'também', 'como', 'bem', 'como', 'mas', 'porém', 'todavia', 'contudo', 'entretanto',  'logo', 'portanto', 'isso', 'assim', 'seguinte', 'que', 'porque', 'pois']
    lstPrepos = ['a', 'ante', 'até', 'após', 'do', 'de', 'desde', 'em', 'entre', 'com', 'contra', 'para', 'pro', 'perante', 'sem', 'sob', 'sobre', 'como', 'conforme', 'segundo', 'durante', 'fora', 'exceto']
    strCodif = ''

    for lstAux in pLst:
        if (lstAux[0].isalpha()):
            if (lstAux in lstArtigos):
                strCodif += 'a'
            elif (lstAux in lstConj):
                strCodif += 'c'
            elif (lstAux in lstPrepos):
                strCodif += 'p'
            elif (lstAux[0].isupper()):
                strCodif += 'M'
            elif (lstAux[0].islower()):
                strCodif += 'm'
        elif (lstAux.isdigit()):
            strCodif += 'N'
        elif (repr(lstAux)):
            strCodif += lstAux
        else:
            strCodif += lstAux
        #fim else
    #fim for

    return strCodif
#fim funcao


# sortTamLst(...) ordena a lista passada por parâmetro em decrescente de tamanho
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


# extraiPadroes(...) extrai certos padroes do texto e retorna uma lista com esses padroes extraidos
def extraiPadroes(pTexto, lstPadroes):
    lstPadroes = sortTamLst(lstPadroes)
    lstTokens, lstPos = tokenizador(pTexto)
    strCodif = codifica(lstTokens)
    lstPadTexto = []

    for pd in range(len(lstPadroes)):
        pos = strCodif.find(lstPadroes[pd])
        while(pos != -1):
            strPal = ''
            strCodif = strCodif.replace(lstPadroes[pd], "*" * len(lstPadroes[pd]), 1)
            for el in range(len(lstPadroes[pd])):
                strPal += lstTokens[pos + el] + " "
            #fim for
            if (strPal):
                lstPadTexto.append(strPal)
            #fim if
            pos = strCodif.find(lstPadroes[pd])
        #fim while
    #fim for
    return lstPadTexto
#fim funcao