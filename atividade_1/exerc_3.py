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
#fim funcao

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

def main():
    texto = "Mesmo sem um trabalho exuberante (a atual passagem no Flamengo é muito boa, por ora) nos últimos anos, Vanderlei é visto pelos atletas como o nome ideal capaz de tirar o time da letargia atual. O perfil boleiro, o conhecimento tático e o sonho de comandar o Tricolor são apontados como pontos que podem suprir Muricy à altura."
    strSeparadores = ' .,:;!?'
    pos = 7

    print(anterior(texto, pos, strSeparadores))
#fim main

main()