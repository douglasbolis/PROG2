__author__ = 'douglas'

import math
# ====================================
# CRIADORES

def criaRetangular(r, i):
    return ([r, i, 1])
# fim funcao

def criaPolar(m, a):
    return ([m, a, 2])
# fim funcao

def getRetangular(numCpx):
    if numCpx[2] == 1:
        return numCpx
    else:
        return [numCpx[0] * math.cos(numCpx[1]), numCpx[1] * math.sin(numCpx[0]), 1]
# fim funcao

def getPolar(numCpx):
    if numCpx[2] == 2:
        return numCpx
    else:
        return [(numCpx[0]**2 + numCpx[1]**2)**0.5, math.atan(numCpx[0]/numCpx[1]), 2]
# fim funcao

def somaNumCpx(numCpxA, numCpxB):
    return [numCpxA[0]+ numCpxB[0], numCpxA[1]+ numCpxB[1], 1]
# fim funcao

def getReal(numCpx):
    return getRetangular(numCpx)[0]
# fim funcao

def getImaginario(numCpx):
    return getRetangular(numCpx)[1]
# fim funcao

# ====================================
# MODIFICADORAS

def setReal(numCpx, r):
    if numCpx[2] == 1:
        numCpx[0] = r
    # fim if
# fim funcao

def setImaginario(numCpx, i):
    if numCpx[2] == 1:
        numCpx[1] = i
    # fim if
# fim funcao

def setModulo(numCpx, m):
    if numCpx[2] == 2:
        numCpx[0] = m
    # fim if
# fim funcao

def setArgumento(numCpx, a):
    if numCpx[2] == 2:
        numCpx[1] = a
    # fim if
# fim funcao

# ====================================
# verificadores

def isRetangular(numCpx):
    return numCpx[2] == 1
# fim funcao

def isPolar(numCpx):
    return numCpx[2] == 2
# fim funcao