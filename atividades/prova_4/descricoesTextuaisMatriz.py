__author__ = 'douglas'

import sys

'''
A função txt2int(<texto com num int>) recebe como entrada um texto descrevendo
um número inteiro entre 0 e 1999 e retorna o equivalente numérico do texto.
Ex.: 'mil e novecentos e noventa e quatro'
ret.: 1994
'''
def txt2int(textoInt):
	lstExt, num, tamMatriz = [], 0, ''
	ext = {
		"um":1, "dois":2, "tres":3, "quatro":4, "cinco":5, "seis":6, "sete":7, "oito":8, "nove":9, "dez":10,
		"onze":11, "doze":12,  "quatorze":14, "quinze":15, "dezesseis":16, "dezessete":17, "dezoito":18, "dezenove":19,
		"vinte":20, "trinta":30, "quarenta":40, "cinquenta":50, "sessenta":60, "setenta":70, "oitenta":80, "noventa":90,
		"cento":100, "duzentos":200, "trezentos":300, "quatrocentos":400, "quinhentos":500, "seiscentos":600, "setecentos":700,
		"oitocentos":800, "novecentos":900, 'mil': 1000
	}

	if textoInt.find(' por ') == -1:
		lstExt = textoInt.strip().split(' e ')

		def convertAuxE(numC, lst):
			if lst == []:
				return numC
			elif lst == ['']:
				return None
			else:
				return convertAuxE(numC + ext[lst[0]], lst[1:])
			# fim else
		# fim convertAuxE

		return convertAuxE(num, lstExt)
	else:
		lstExt = textoInt.strip().split(' por ')

		def convertAuxPor(tamM, lst):
			if lst == []:
				return tamM
			else:
				return convertAuxPor(tamM + str(ext[lst[0]]), lst[1:])
		# fim convertAuxPor

		return convertAuxPor(tamMatriz, lstExt)
	# fim else

# fim txt2int

'''
A função txt2mat(<descrição textual da matriz>) recebe como parâmetro de entrada a
descrição textual de uma matriz e retorna o equivalente numérico da
matriz utilizando lista.
Ex.: 'dois por dois;duzentos e setenta e dois;novecentos e sessenta e seis;trezentos e setenta e quatro;mil e duzentos e vinte e sete;'
ret.: [[262, 966], [364, 1227]]
'''
def txt2mat(txtMatriz):
	lstMat, mat = [], []
	lstTxtMatriz = txtMatriz.strip().split(';')
	i, j, aux = 0, 0, 0

	for el in lstTxtMatriz:
		lstMat.append(txt2int(el))
	# fim for

	i, j = int(lstMat[0][0]), int(lstMat[0][1])
	lstMat = lstMat[1:-1]

	for x in range(i):
		mat.append([])
		for y in range(j):
			mat[x].append(lstMat[aux])
			aux += 1
		# fim for
	# fim for

	return mat
# fim txt2mat

'''
A função det(<param matriz inteiros>) calcula e retorna o valor do determinante da matriz
quadrada de inteiros passada como parâmetro de entrada. Essa função foi implementada utilizando
recursidade junto com o algoritmo de LaPlace para efetuar os cálculo.
'''
def det(matrizInt):
	coef, detMatriz = 0, 0
	lin, col = len(matrizInt), len(matrizInt[0])

	if lin == col and lin > 0:
		detMatriz = 0
		lstElemMatriz = []

		if(lin >= 2):
			lstElemTemp = []

			for linha in range(1, lin + 1):
				coluna = 1
				coef = ((-1)**(linha+coluna)) * matrizInt[linha-1][coluna-1]
				lstElemTemp.append(coef * det(getSubMatriz(matrizInt,linha,coluna)))
			# fim for

			lstElemMatriz = lstElemTemp
		else:
			lstElemMatriz.append(matrizInt[0][0])
		# fim else

		for el in lstElemMatriz:
			detMatriz = detMatriz + el
		# fim for
	else:
		print('a matrizInt nao é quadrada')
	# fim else

	return detMatriz
# fim det

#(submatriz para calculo de laplace) com o objetivo de reduzir a matriz para fazer o metodo de laplace
# Retorna submatrizes para o calculo
def getSubMatriz(matriz, linhaExcl, colunaExcl):
	subMatriz = [lin[:] for lin in matriz]
	del subMatriz[linhaExcl - 1]
	for lin in subMatriz: del lin[colunaExcl - 1]
	
	return subMatriz
# fim subMatriz

def main():
	if (len(sys.argv) == 3):
		arqRead = open(sys.argv[1], 'rt')
		arqWrite = open(sys.argv[2], 'wt')

		pos = arqRead.tell()
		linha = arqRead.readline()

		while linha != '':
			arqWrite.write(str(det(txt2mat(linha))) + ', ' + str(pos) + '\n')

			pos = arqRead.tell()
			linha = arqRead.readline()
		# fim while

		arqRead.close()
		arqWrite.close()
	else:
		print("\nQuantidade de parametros incorreto\n")
		print("Use: python3 <nome do arquivo txt com contendo descrição textuais de matrizes> ", end="")
		print("<nome do arquivo ndx para salvar o resultado das determinantes>\n\n")
	#fim else
# fim main

main()