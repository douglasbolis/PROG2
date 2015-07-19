__author__ = 'douglas'

import math

# A função "criar(<float real>,<float img>)" cria e retorna um TAD Complexo a partir dos valores de
# entrada representando a parte real e a parte imaginária do número complexo.
# EX.:  criar(2.0, 3.0)  -->  {"real": 2.0, "imaginario": 3.0}
#
def criar(r, i):
	return {"real": r, "imaginario": i}
# fim criar

# A função "criarP(<float modulo>,<float ang>)" cria e retorna um TAD Complexo a partir dos valores
# de entrada representando o módulo e o ângulo do número complexo (forma polar).
# Internamente deve ser convertido para a forma retangular.
# EX.:  criaP(3.6056, 56.310)  -->  criar(2.0, 3.0) --> {"real": 2.0, "imaginario": 3.0}
#
def criaP(m, a):
	return criar(m * math.cos(math.radians(a)), m * math.sin(math.radians(a)))
# fim criarP

# A função "criaStr(<string>)" cria e retorna um TAD Complexo a partir de uma string de entrada com
# conteúdo sempre na forma 'n+mi', onde n e m são valores reais quaisquer representando a
# parte real e a parte imaginaria do número complexo.
# EX.:  criaStr('4.5+5.25i')  -->  cria(4.5, 5.25)  -->  {"real": 4.5, "imaginario": 5.25}
#
def criaStr(strComplexo):
	if (strComplexo.find('+') > 0):
		lstStrComplexo = strComplexo.strip().split('+')
		return criar(float(lstStrComplexo[0]), float(lstStrComplexo[1][:-1]))
	else:
		lstStrComplexo = strComplexo.strip().split('-')
		if (strComplexo[0] == '-'):
			return criar(-1 * float(lstStrComplexo[1]), -1 * float(lstStrComplexo[2][:-1]))
		else:
			return criar(float(lstStrComplexo[0]), -1 * float(lstStrComplexo[1][:-1]))
		# fim if
	#  fim else
# fim criaStr


#############	TERMINAR DAQUI	####################
def soma(numCpxA, numCpxB):
	return criar(numCpxA["real"] + numCpxB["real"], numCpxA["imaginario"] + numCpxB["imaginario"])
# fim soma

def multi(numCpxA, numCpxB):
	return [numCpxA[0] * numCpxB[0], numCpxA[1] * numCpxB[1]]
# fim multi

def divid(numCpxA, numCpxB):
	return [numCpxA[0] / numCpxB[0], numCpxA[1] / numCpxB[1]]
# fim divid

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
# fim getStr