__author__ = 'douglas'

import math

def criar(r, i):
	return ([r, i])
# fim funcao

def criaP(m, a):
	return [m * math.cos(rad(a)), rad(a) * math.sin(m)]
# fim funcao

def criaStr(strComplexo):
	if (strComplexo.find('+') > 0):
		lstStrComplexo = strComplexo.strip().split('+')
		return ([float(lstStrComplexo[0]), float(lstStrComplexo[1][:-1])])
	elif (strComplexo.find('-') > 0):
		lstStrComplexo = strComplexo.strip().split('-')
		return ([float(lstStrComplexo[0]), float(lstStrComplexo[1][:-1])])
	# fim elif
	return []
# fim funcao

def soma(numCpxA, numCpxB):
    return [numCpxA[0] + numCpxB[0], numCpxA[1] + numCpxB[1]]
# fim funcao

def multi(numCpxA, numCpxB):
    return [numCpxA[0] * numCpxB[0], numCpxA[1] * numCpxB[1]]
# fim funcao

def divid(numCpxA, numCpxB):
    return [numCpxA[0] / numCpxB[0], numCpxA[1] / numCpxB[1]]
# fim funcao

def vezesK(numCpxA, k):
    return [numCpxA[0] * k, numCpxA[1] * k]
# fim funcao

def getStr(numCpx):
	strComplexo = str(numCpx[0])
	
	if (int(numCpx[1]) > 0):
		strComplexo += '+' + str(numCpx[1][:-1] + 'i')
	elif (int(numCpx[1]) < 0):
		strComplexo += '-' + str((-1)*int(numCpx[1][:-1]) + 'i')
	# fim else
	
    return strComplexo
# fim funcao
