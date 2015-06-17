__author__ = 'douglas'

def criar(x,y):
    """Retorna um tad ponto a partir das coordenadas x,y do ponto no plano
    cartesiano."""
    return (x, y)
# fim função

def distancia(paramTADptoA, paramTADptoB):
    """Retorna um float com a distância euclidiana entre dois tad pontos."""
    return (((paramTADptoA[0] - paramTADptoB[0])**2) + ((paramTADptoA[1] - paramTADptoB[1])**2))**(1/2)
# fim função

def getXY(paramTADpto):
    """Retorna uma tupla com as coordenadas x e y do ponto."""
    return (paramTADpto[0], paramTADpto[1])
# fim função

def igual(paramTADptoA, paramTADptoB):
    """Retorna boolean True se os dois tad ponto de entrada forem iguais
    (mesmo valores de coordenadas):, False caso contrário."""
    return paramTADptoA[0] == paramTADptoB[0] and paramTADptoA[1] == paramTADptoB[1]
# fim função

def move(paramTADpto, dx, dy):
    """Desloca, no plano, o ponto de dx na coordenada x e de dy na
    coordenada y."""
    return (paramTADpto[0] + dx, paramTADpto[1] + dy)
# fim função

def intersec(paramTADretA, paramTADretB):
    """Retorna um tad retângulo que é a intersecção dos dois retângulo de
    entrada, ou None se os retângulo de entrada não se intercederem."""
    """if ():

    elif ():

    else:"""

    # fim else
# fim função
