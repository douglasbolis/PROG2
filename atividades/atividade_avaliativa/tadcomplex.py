__author__ = 'douglas'

import math

# A função "criar(<float real>,<float img>)" cria e retorna um TAD Complexo a partir dos valores de
# entrada representando a parte real e a parte imaginária do número complexo.
# EX.:
# 	criar(2.0, 3.0)
# 	{"real": 2.0, "imaginario": 3.0}
#
def criar(r, i):
	return {"real": r, "imaginario": i}
# fim criar

# A função "criarP(<float modulo>,<float ang>)" cria e retorna um TAD Complexo a partir dos valores
# de entrada representando o módulo e o ângulo do número complexo (forma polar).
# Internamente deve ser convertido para a forma retangular.
# EX.:
# 	criaP(3.6056, 56.310)
# 	criar(2.0, 3.0)
# 	{"real": 2.0, "imaginario": 3.0}
#
def criaP(m, a):
	return criar(m * math.cos(math.radians(a)), m * math.sin(math.radians(a)))
# fim criarP

# A função "criaStr(<string>)" cria e retorna um TAD Complexo a partir de uma string de entrada com
# conteúdo sempre na forma 'n+mi', onde n e m são valores reais quaisquer representando a
# parte real e a parte imaginaria do número complexo.
# EX.:
# 	criaStr('4.5+5.25i')
# 	criar(4.5, 5.25)
# 	{"real": 4.5, "imaginario": 5.25}
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

# A função "soma(<tadComplexA>,<tadComplexB>)" retorna um número complexo (TAD Complexo)
# que é a soma dos números complexos de entrada.
# EX.:
# 	soma({"real": 6, "imaginario": 5}, {"real": 2, "imaginario": -1})
# 	criar(6 + 2, 5 + (-1))
# 	{"real": 8, "imaginario": 4}
#
def soma(numCpxA, numCpxB):
	return criar(numCpxA["real"] + numCpxB["real"], numCpxA["imaginario"] + numCpxB["imaginario"])
# fim soma

# A função "multip(<tadComplexA>,<tadComplexB>)" retorna um número complexo (TAD Complexo)
# que é o produto dos números complexos de entrada.
# EX.:
# 	multi({"real": 5, "imaginario": 1}, {"real": 2, "imaginario": -1})
# 	criar((5*2 - 1*(-1), 5*(-1) + 1*2)
# 	{"real": 11, "imaginario": -3}
#
def multi(numCpxA, numCpxB):
	return  criar(
		numCpxA["real"] * numCpxB["real"] - numCpxA["imaginario"] * numCpxB["imaginario"],
		numCpxA["real"] * numCpxB["imaginario"] + numCpxA["imaginario"] * numCpxB["real"]
	)
# fim multi

# A função "divid(<tadComplexA>,<tadComplexB>)" retorna um número complexo (TAD Complexo)
# que é a divisão dos números complexos de entrada
# EX.:
# 	divid({"real": 5, "imaginario": 1}, {"real": 2, "imaginario": -1})
#	criar((5*2 + 1*(-1)) / (2² + (-1)²), (2*1 - 5*(-1)) / (2² + (-1)²))
#	{"real": 1.8, "imaginario": 1.4}
#
def divid(numCpxA, numCpxB):
	return criar(
		(numCpxA["real"] * numCpxB["real"] + numCpxA["imaginario"] * numCpxB["imaginario"]) / (numCpxB["real"]**2 + numCpxB["imaginario"]**2),
		(numCpxB["real"] * numCpxA["imaginario"] - numCpxA["real"] * numCpxB["imaginario"]) / (numCpxB["real"]**2 + numCpxB["imaginario"]**2)
	)
# fim divid

# A função "vezesK(<tadComplexA>,<k float>)" retorna um número complexo (TAD Complexo) cujos
# componentes foram multiplicados por um valor qualquer float k.
# EX.:
# 	vezesK({"real": 1.8, "imaginario": 1.4}, 10)
# 	criar(18, 14)
# 	{"real": 18, "imaginario": 14}
#
def vezesK(numCpxA, k):
	return criar(numCpxA["real"] * k, numCpxA["imaginario"] * k)
# fim funcao

# A função "getStr(<tadComplexA>)" retorna o número complexo como uma string com o seguinte
# formato: “r+mi”, sem espaços, onde r e m são números reais (1 casa decimal apenas)
# representando as partes reais e imaginárias do número complexo.
# EX.:
# 	getStr({"real": 1.8, "imaginario": 1.4})
#	“1.8+1.4i”
#
def getStr(numCpx):
	strComplexo = "%.1f" %(numCpx["real"])

	if (float(numCpx["imaginario"]) >= 0):
		strComplexo += "+%.1fi" %(numCpx["imaginario"])
	elif (float(numCpx["imaginario"]) < 0):
		strComplexo += "%.1fi" %(numCpx["imaginario"])
	# fim else

	return strComplexo
# fim getStr