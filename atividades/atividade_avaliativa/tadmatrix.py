__author__ = 'Douglas'

import tadcomplex

# A função "criar(<altura int>,<largura int>)" cria e retorna um TMC de altura e largura definida pelos
# parâmetros de entrada. O conteúdo de uma matriz recém-criada são elementos iguais ao
# valor zero complexo (0 + 0i).
#
def criar(altA, altB):
	dicMatrix = {}

	dicMatrix["lin"] = altA
	dicMatrix["col"] = altB

	for i in range(altA):
		for j in range(altB):
			dicMatrix["%d%d" %(i+1, j+1)] = '0+0i'
		# fim for
	# fim for
	
	return dicMatrix
# fim criar

# A função "adElem(<paramTMC>,<linha int>,<coluna int>,<tadComplex>)" altera a TMC de entrada
# para que seu elemento de coordenadas linha, coluna armazene o valor de número complexo
# igual ao parâmetro tadComplex
#
def adElem(paramTMC,linha,coluna,tadComplex):
	paramTMC["%d%d" %(linha, coluna)] = tadcomplex.getStr(tadComplex)
# fim adElem

# A função "getElem(<paramTMC>,<linha int>,<coluna int>)" retorna o elemento TAD Complexo
# residente na posição linha, coluna do parâmetro TMC de entrada.
#
def getElem(paramTMC,linha,coluna):
	return tadcomplex.criaStr(paramTMC["%d%d" %(linha, coluna)])
# fim getElem

# A função "getLinhasTMC(<paramTMC>)" retorna a quantidade de linhas da TMC
# parâmetro de entrada.
#
def getLinhasTMC(paramTMC):
	return paramTMC["lin"]
# fim getLinhasTMC

# A função "getColunasTMC(<paramTMC>)" retorna a quantidade de colunas da TMC
# parâmetro de entrada
#
def getColunasTMC(paramTMC):
	return paramTMC["col"]
# fim getColunasTMC

# A função "imprimeTMC(<paramTMC>)" faz a impressão organizada na forma matricial da TMC
# passada como parâmetro de entrada.
#
def imprimeTMC(paramTMC):
	for i in range(paramTMC["lin"]):
		for j in range(paramTMC["col"]):
			print(paramTMC["%d%d" %(i+1, j+1)] + "	", end="")
		# fim for
		print()
	# fim for
# fim imprimeTMC