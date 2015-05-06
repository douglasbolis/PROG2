__author__ = 'douglas'


"""     FUNÇÕES DE MANIPULAÇÃO DE TEXTOS    """

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

#   tabFreg(...) transforma o texto em uma lista e chama geraTabFreg(...)
def tabFreg(pTexto, srtSep):
    lst = separaPalavras(pTexto, srtSep)
    geraTabFreg(lst)
#fim funcao

#   geratabFreg(...) imprime a tabela de frequencia da lista passada por parâmetro
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