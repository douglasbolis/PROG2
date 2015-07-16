__author__ = 'douglas'

import math

def criar(xcentro,ycentro,raio):
    '''Retorna um tad retângulo a partir da origem (canto superior
esquerdo): e da extremidade direita inferior.'''

    return [xcentro-raio, ycentro-raio, xcentro+raio, ycentro+raio]
# fim funcao

def getCentro(paramTADcirc):
    '''Retorna um tad ponto com as coordenadas do centro do círculo.'''

    return [paramTADcirc[0], paramTADcirc[1]]
# fim funcao

def getRaio(paramTADcirc):
    '''Retorna um float com o tamanho do raio usado para a criação do
círculo.'''

    return float(paramTADcirc[2])
# fim funcao

def perimetro(paramTADcirc):
    '''Retorna um float com o valor do perímetro.'''

    return float(2 * math.pi * paramTADcirc[2])
# fim funcao

def area(paramTADcirc):
    '''Retorna um float com a área do retângulo.'''

    return float(math.pi * (paramTADcirc[2] ** 2))
# fim funcao

def move(paramTADcircA, dx, dy):
    '''Desloca o círculo no plano (sua origem): de dx na coordenada x e dy
na coordenada y.'''

    return [paramTADcircA[0] + dx, paramTADcircA[1] + dy, paramTADcircA[2]]
# fim funcao

def contido(paramTADcircA, paramTADcircB):
    '''Retorna um boolean True se o circulo A está totalmente contido no
círculo B, False caso contrário.'''

    # if (paramTADcircA):
    #
    # # fim if
    # return
# fim funcao