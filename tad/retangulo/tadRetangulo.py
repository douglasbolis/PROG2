__author__ = 'douglas'

def criarVtx(xsupesq,ysupesq,xinfd,yinf):
    '''cria via vértices.
    Retorna um tad retângulo a partir da origem (canto superior
    esquerdo) e da extremidade direita inferior.'''
    return (xsupesq,ysupesq,xinfd,yinf)
# fim funcao

def criarDim(xsupesq,ysupesq,larg,alt):
    '''cria via origem e dimensões.
    Retorna um tad retângulo a partir da origem (canto superior
    esquerdo) e da largura e altura.'''
    return (xsupesq,ysupesq,larg,alt)
# fim funcao

def getCantos(paramTADret):
    '''Retorna uma lista de tad pontos com os cantos superior esquerdo e
    inferior direito, respectivamente.'''
    return (paramTADret[0], paramTADret[1], paramTADret[2], paramTADret[3])
# fim funcao

def perimetro(paramTADret):
    '''Retorna um float com o valor do perímetro.'''
    return float((2 * (paramTADret[2] - paramTADret[0])) + (2 * (paramTADret[3] - paramTADret[1])))
# fim funcao

def area(paramTADret):
    '''Retorna um float com a área do retângulo.'''
    return float((2 * (paramTADret[2] - paramTADret[0])) + (2 * (paramTADret[3] - paramTADret[1])))
# fim funcao

def igual(paramTADretA, paramTADretB):
    '''Retorna boolean True se os dois retângulos de entrada forem iguais
    (mesmo valores de lados), False caso contrário.'''
    return (paramTADretA[2] - paramTADretA[0]) == (paramTADretB[2] -paramTADretB[0]) and (paramTADretA[3] - paramTADretA[1]) == (paramTADretB[3] -paramTADretB[1])
# fim funcao

def move(paramTADretA, dx, dy):
    '''Desloca, no plano, o retângulo (sua origem) de dx na coordenada x e
    dy na coordenada y.'''
    return (paramTADretA[0] + dx, paramTADretA[1] + dy, paramTADretA[2] + dx, paramTADretA[3] + dy)
# fim funcao

def intersec(paramTADretA, paramTADretB):
    '''Retorna um tad retângulo que é a intersecção dos dois retângulo de
    entrada, ou None se os retângulo de entrada não se intercederem.'''

    intRets = []
    cantoSupEsqA = (paramTADretA[0], paramTADretA[1])
    cantoSupEsqB = (paramTADretB[0], paramTADretB[1])

    cantoInfEsqA = (paramTADretA[0], paramTADretA[3])
    cantoInfEsqB = (paramTADretB[0], paramTADretB[3])

    cantoSupDirA = (paramTADretA[2], paramTADretA[1])
    cantoSupDirB = (paramTADretB[2], paramTADretB[1])

    cantoInfDirA = (paramTADretA[2], paramTADretA[3])
    cantoInfDirB = (paramTADretB[2], paramTADretB[3])

    # se A esta dentro de B
    if (
        (cantoSupEsqA[0] >= cantoSupEsqB[0] and cantoSupEsqA[1] >= cantoSupEsqB[1]) and
        (cantoInfDirA[0] <= cantoInfDirB[0] and cantoInfDirA[1] <= cantoInfDirB[1])
    ):
        return paramTADretA

    # se B esta dentro de A
    elif (
        (cantoSupEsqB[0] >= cantoSupEsqA[0] and cantoSupEsqB[1] >= cantoSupEsqA[1]) and
        (cantoInfDirB[0] <= cantoInfDirA[0] and cantoInfDirB[1] <= cantoInfDirA[1])
    ):
        return paramTADretB

    # lado baixo de a com lado cima de b
    elif (
        (cantoInfDirB[0] >= cantoSupEsqA[0] and cantoInfDirB[1] >= cantoSupEsqA[1]) and
        (cantoSupEsqB[0] <= cantoSupEsqA[0] and cantoSupEsqB[1] <= cantoSupEsqA[1]) and
        (cantoInfDirA[0] <= cantoInfDirB[0] and cantoInfDirA[1] >= cantoInfDirB[1])
    ):
        return [cantoSupEsqA[0], cantoSupEsqA[1], cantoInfDirA[0], cantoInfDirB[1]]
########################################
    # lado esquerdo de b com lado direito de a
    elif (
        (cantoInfDirA[0] >= cantoSupEsqB[0] and cantoInfDirA[1] >= cantoSupEsqB[1]) and
        (cantoSupEsqA[0] <= cantoSupEsqB[0] and cantoSupEsqA[1] <= cantoSupEsqB[1]) and
        (cantoInfDirB[0] >= cantoInfDirA[0] and cantoInfDirB[1] <= cantoInfDirA[1])
    ):
        return [cantoSupEsqB[0], cantoSupEsqB[1], cantoInfDirA[0], cantoInfDirB[1]]

    # lado esquerdo de a com lado direito de b
    elif (
        (cantoInfDirB[0] >= cantoSupEsqA[0] and cantoInfDirB[1] >= cantoSupEsqA[1]) and
        (cantoSupEsqB[0] <= cantoSupEsqA[0] and cantoSupEsqB[1] <= cantoSupEsqA[1]) and
        (cantoInfDirA[0] >= cantoInfDirB[0] and cantoInfDirA[1] <= cantoInfDirB[1])
    ):
        return [cantoSupEsqA[0], cantoSupEsqA[1], cantoInfDirB[0], cantoInfDirA[1]]
    ##
    # lado esquerdo de b com lado direito de a
    elif (
        (cantoInfDirA[0] >= cantoSupEsqB[0] and cantoInfDirA[1] >= cantoSupEsqB[1]) and
        (cantoSupEsqA[0] <= cantoSupEsqB[0] and cantoSupEsqA[1] <= cantoSupEsqB[1]) and
        (cantoInfDirB[0] >= cantoInfDirA[0] and cantoInfDirB[1] <= cantoInfDirA[1])
    ):
        return [cantoSupEsqB[0], cantoSupEsqB[1], cantoInfDirA[0], cantoInfDirB[1]]

    # lado esquerdo de a com lado direito de b
    elif (
        (cantoInfDirB[0] >= cantoSupEsqA[0] and cantoInfDirB[1] >= cantoSupEsqA[1]) and
        (cantoSupEsqB[0] <= cantoSupEsqA[0] and cantoSupEsqB[1] <= cantoSupEsqA[1]) and
        (cantoInfDirA[0] >= cantoInfDirB[0] and cantoInfDirA[1] <= cantoInfDirB[1])
    ):
        return [cantoSupEsqA[0], cantoSupEsqA[1], cantoInfDirB[0], cantoInfDirA[1]]

    #################################

    # canto superior esquerdo de b com canto inferior direito de a
    elif (
        (cantoInfDirA[0] >= cantoSupEsqB[0] and cantoInfDirA[1] >= cantoSupEsqB[1]) and
        (cantoSupEsqA[0] <= cantoSupEsqB[0] and cantoSupEsqA[1] <= cantoSupEsqB[1])
    ):
        return [cantoSupEsqB[0], cantoSupEsqB[1], cantoInfDirA[0], cantoInfDirA[1]]

    # canto superior esquerdo de b com canto inferior direito de a
    elif (
        (cantoInfDirB[0] >= cantoSupEsqA[0] and cantoInfDirB[1] >= cantoSupEsqA[1]) and
        (cantoSupEsqB[0] <= cantoSupEsqA[0] and cantoSupEsqB[1] <= cantoSupEsqA[1])
    ):
        return [cantoSupEsqA[0], cantoSupEsqA[1], cantoInfDirB[0], cantoInfDirB[1]]

################################################

    # lado baixo de b com lado cima de a
    elif (
        (cantoSupEsqB[0] >= cantoSupEsqA[0] and cantoSupEsqB[1] <= cantoSupEsqA[1]) and
        (cantoInfDirB[0] <= cantoSupDirA[0] and cantoInfDirB[1] >= cantoSupDirA[1])
    ):
        return [cantoSupEsqB[0], cantoSupEsqB[1], cantoInfDirB[0], cantoInfDirA[1]]

####################################

    # canto superior direito de a com canto inferior esquerdo de b
    elif (
        (cantoInfDirB[0] >= cantoSupEsqA[0] and cantoInfDirB[1] >= cantoSupEsqA[1]) and
        (cantoSupEsqB[0] <= cantoSupEsqA[0] and cantoSupEsqB[1] <= cantoSupEsqA[1])
    ):
        return [cantoInfEsqB[0], cantoInfEsqB[1], cantoSupDirA[0], cantoSupDirA[1]]

    # canto superior direito de b com canto inferior esquerdo de a
    # # elif (
    # #     (cantoInfEsqA[0] <= cantoSupDirB[0] and cantoInfEsqA[1] >= cantoSupDirB[1]) and
    # #     (cantoInfEsqA[0] >= cantoInfEsqB[0] and cantoInfEsqA[1] >= cantoSupEsqB[1])
    # # ):
    #     return [cantoInfEsqA[0], cantoInfEsqA[1], cantoSupDirB[0], cantoSupDirB[1]]
    # fim elif

    return intRets
# fim funcao
