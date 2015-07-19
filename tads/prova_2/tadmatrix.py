__author__ = 'Douglas'

import tadcomplex

def criar(altA, altB):
	lstMatrix = []
	
	for i in range(altA):
		lstAuxMatrix = []
		for j in range(altB):
			lstAuxMatrix.append('0+0i')
		# fim for
		lstMatrix.append(lstAuxMatrix)
	# fim for
	
	return lstMatrix	
# fim funcao

def adElem(paramTMC,linha,coluna,tadComplex):

	paramTMC[linha][coluna] = tadcomplex.getStr(tadComplex)

# fim funcao

def getElem(paramTMC,linha,coluna):
	return paramTMC[linha][coluna]
# fim funcao

def getLinhasTMC(paramTMC):
	return len(paramTMC)
# fim funcao

def getColunasTMC(paramTMC):
	return len(paramTMC[0])
# fim funcao

def multiTMC(paramTMCa, paramTMCb):
	novaTadMatrix = []

	for i in range(len(paramTMCa)):
		lstAuxTadMatrix = []
		for j in range(len(paramTMCa[i])):
			lstAuxTadMatrix.append(paramTMCa[i][j]*paramTMCb[j][i])
		# fim for
		novaTadMatrix.append(lstAuxTadMatrix)
	# fim for
	return novaTadMatrix
# fim funcao
