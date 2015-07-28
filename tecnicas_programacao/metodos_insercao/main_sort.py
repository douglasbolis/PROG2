__author__ = 'douglas'

import random
import insercao_direta
import insercao_bolha
import insercao_selecao

def geraLista(tamLst):
	lst_resultados = []
	i = 0

	while i < tamLst:
		num = random.randint(0, 200000)

		if num not in lst_resultados:
			lst_resultados.append(num)
			i += 1
		# fim if
	# fim while

	return lst_resultados
# fim geraLista

def main():

	lstTam = [
		20, 80, 180, 320, 500, 720, 980, 1280, 1620, 2000, 2420, 2880, 3380, 3920, 4500, 5120,
		5780, 6480, 7220, 8000, 8820, 9680, 10580, 11520, 12500, 13520, 14580, 15680, 16820, 18000
	]

	arqTabela = open('tabela_sort.csv', 'wt')
	arqTabela.write('Length of List|Bubble|Selection|Insertion\n')

	for i in lstTam:
		novaLst = geraLista(i)

		lstBubble = novaLst[:]
		lstInsertion = novaLst[:]
		lstSelection = novaLst[:]

		arqTabela.write(
			str(i) + '|' + \
			str(insercao_bolha.bubbleSort(lstBubble)[1]) + '|' + \
			str(insercao_selecao.selectionSort(lstSelection)[1]) + '|' + \
			str(insercao_direta.insertionSort(lstInsertion)[1]) + '\n'
		)
	# fim for

	arqTabela.close()

	# if ((lst[linha][cidade] > lst[linha+1][cidade]) or
	#    ((lst[linha][cidade] == lst[linha+1][cidade]) and (lst[linha][bairro] > lst[linha+1][bairro])) or
	# 	((lst[linha][cidade] == lst[linha+1][cidade]) and (lst[linha][bairro] == lst[linha+1][bairro]) and (lst[linha][logradouro] > lst[linha+1][logradouro]))

# fim main

main()