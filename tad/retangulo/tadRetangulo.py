__author__ = 'douglas'

def criarVtx(xsupesq,ysupesq,xinfd,yinf):
    '''cria via vértices.
    Retorna um tad retângulo a partir da origem (canto superior
    esquerdo) e da extremidade direita inferior.'''
    return [xsupesq,ysupesq,xinfd,yinf]
# fim funcao

def criarDim(xsupesq,ysupesq,larg,alt):
    '''cria via origem e dimensões.
    Retorna um tad retângulo a partir da origem (canto superior
    esquerdo) e da largura e altura.'''
    return [xsupesq,ysupesq,larg,alt]
# fim funcao

def getCantos(paramTADret):
    '''Retorna uma lista de tad pontos com os cantos superior esquerdo e
    inferior direito, respectivamente.'''
    return [paramTADret[0], paramTADret[1], paramTADret[2], paramTADret[3]]
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

    # se A está dentro de B
    if (
        supEsqDentro(paramTADretA, paramTADretB) and supDirDentro(paramTADretA, paramTADretB) and
        infEsqDentro(paramTADretA, paramTADretB) and infDirDentro(paramTADretA, paramTADretB)
    ):
      return paramTADretA

    # se B está dentro de A
    elif (
        supEsqDentro(paramTADretB, paramTADretA) and supDirDentro(paramTADretB, paramTADretA) and
        infEsqDentro(paramTADretB, paramTADretA) and infDirDentro(paramTADretB, paramTADretA)
    ):
        return paramTADretB

    # se superior direito de A esta em B / ou / inferior esquerdo de B esta em A
    elif (
        not supEsqDentro(paramTADretA, paramTADretB) and supDirDentro(paramTADretA, paramTADretB) and
        not infEsqDentro(paramTADretA, paramTADretB) and not infDirDentro(paramTADretA, paramTADretB)
    ):
        return [paramTADretB[0], paramTADretA[1], paramTADretA[2], paramTADretB[3]]

    # se superior direito de B esta em A / ou / inferior esquerdo de A esta em B
    elif (
        not supEsqDentro(paramTADretB, paramTADretA) and supDirDentro(paramTADretB, paramTADretA) and
        not infEsqDentro(paramTADretB, paramTADretA) and not infDirDentro(paramTADretB, paramTADretA)
    ):
        return [paramTADretA[0], paramTADretB[1], paramTADretB[2], paramTADretA[3]]

    # se superior esquerdo de A esta em B / ou / inferior direito de B esta em A
    elif (
        supEsqDentro(paramTADretA, paramTADretB) and not supDirDentro(paramTADretA, paramTADretB) and
        not infEsqDentro(paramTADretA, paramTADretB) and not infDirDentro(paramTADretA, paramTADretB)
    ):
        return [paramTADretA[0], paramTADretA[1], paramTADretB[2], paramTADretB[3]]

    # se superior esquerdo de B esta em A / ou / inferior direito de A esta em B
    elif (
        supEsqDentro(paramTADretB, paramTADretA) and not supDirDentro(paramTADretB, paramTADretA) and
        not infEsqDentro(paramTADretB, paramTADretA) and not infDirDentro(paramTADretB, paramTADretA)
    ):
        return [paramTADretB[0], paramTADretB[1], paramTADretA[2], paramTADretA[3]]

    # se lado de baixo de A esta em B
    elif (
        not supEsqDentro(paramTADretA, paramTADretB) and not supDirDentro(paramTADretA, paramTADretB) and
        infEsqDentro(paramTADretA, paramTADretB) and infDirDentro(paramTADretA, paramTADretB)
    ):
        return [paramTADretA[0], paramTADretB[1], paramTADretA[2], paramTADretA[3]]

    # se lado de baixo de B esta em A
    elif (
        not supEsqDentro(paramTADretB, paramTADretA) and not supDirDentro(paramTADretB, paramTADretA) and
        infEsqDentro(paramTADretB, paramTADretA) and infDirDentro(paramTADretB, paramTADretA)
    ):
        return [paramTADretB[0], paramTADretA[1], paramTADretB[2], paramTADretB[3]]

    # se lado de cima de A esta em B
    elif (
        supEsqDentro(paramTADretA, paramTADretB) and supDirDentro(paramTADretA, paramTADretB) and
        not infEsqDentro(paramTADretA, paramTADretB) and not infDirDentro(paramTADretA, paramTADretB)
    ):
        return [paramTADretA[0], paramTADretA[1], paramTADretA[2], paramTADretB[3]]

    # se lado de cima de B esta em A
    elif (
        supEsqDentro(paramTADretB, paramTADretA) and supDirDentro(paramTADretB, paramTADretA) and
        not infEsqDentro(paramTADretB, paramTADretA) and not infDirDentro(paramTADretB, paramTADretA)
    ):
        return [paramTADretB[0], paramTADretB[1], paramTADretB[2], paramTADretA[3]]

    # se lado direito de A esta em B
    elif (
        not supEsqDentro(paramTADretA, paramTADretB) and supDirDentro(paramTADretA, paramTADretB) and
        not infEsqDentro(paramTADretA, paramTADretB) and infDirDentro(paramTADretA, paramTADretB)
    ):
        return [paramTADretB[0], paramTADretA[1], paramTADretA[2], paramTADretA[3]]

    # se lado direito de B esta em A
    elif (
        not supEsqDentro(paramTADretB, paramTADretA) and supDirDentro(paramTADretB, paramTADretA) and
        not infEsqDentro(paramTADretB, paramTADretA) and infDirDentro(paramTADretB, paramTADretA)
    ):
        return [paramTADretA[0], paramTADretB[1], paramTADretB[2], paramTADretB[3]]

    # se lado esquerdo de A esta em B
    elif (
        supEsqDentro(paramTADretA, paramTADretB) and not supDirDentro(paramTADretA, paramTADretB) and
        infEsqDentro(paramTADretA, paramTADretB) and not infDirDentro(paramTADretA, paramTADretB)
    ):
        return [paramTADretA[0], paramTADretA[1], paramTADretB[2], paramTADretA[3]]

    # se lado esquerdo de B esta em A
    elif (
        supEsqDentro(paramTADretB, paramTADretA) and not supDirDentro(paramTADretB, paramTADretA) and
        infEsqDentro(paramTADretB, paramTADretA) and not infDirDentro(paramTADretB, paramTADretA)
    ):
        return [paramTADretB[0], paramTADretB[1], paramTADretA[2], paramTADretB[3]]

    # se os retângulos estão cruzados como sinal de soma
    elif (especialDentro(paramTADretA, paramTADretB)):
        return [paramTADretA[0], paramTADretB[1], paramTADretA[2], paramTADretB[3]]

    # se os retângulos estão cruzados como sinal de soma
    elif (especialDentro(paramTADretB, paramTADretA)):
        return [paramTADretB[0], paramTADretA[1], paramTADretB[2], paramTADretA[3]]
    # fim elif

    return intRets
# fim funcao

def supEsqDentro(retA, retB): # OK
    return (retA[0] >= retB[0] and retA[1] >= retB[1]) and (retA[0] <= retB[2] and retA[1] <= retB[3])
# fim funcao

def supDirDentro(retA, retB): # OK
    return (retA[2] <= retB[2] and retA[1] >= retB[1]) and (retA[2] >= retB[0] and retA[1] <= retB[3])
# fim funcao

def infEsqDentro(retA, retB): # OK
    return (retA[0] >= retB[0] and retA[3] <= retB[3]) and (retA[0] <= retB[2] and retA[3] >= retB[1])
# fim funcao

def infDirDentro(retA, retB): # OK
    return (retA[2] <= retB[2] and retA[3] <= retB[3]) and (retA[2] >= retB[0] and retA[3] >= retB[1])
# fim funcao

def especialDentro(retA, retB):
    return (
        (not supEsqDentro(retA, retB) and not supDirDentro(retA, retB) and not infDirDentro(retA, retB) and not infEsqDentro(retA, retB)) and
        (retB[0] <= retA[0] and retB[1] >= retA[1]) and (retB[0] <= retA[0] and retB[3] <= retA[3]) and
        (retB[2] >= retA[2] and retB[1] >= retA[1]) and (retB[2] >= retA[2] and retB[3] <= retA[3])
    )
# fim funcao