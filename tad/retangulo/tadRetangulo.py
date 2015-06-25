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