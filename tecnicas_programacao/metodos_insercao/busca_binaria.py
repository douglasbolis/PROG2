__author__ = 'douglas'

import insercao_direta
import insercao_bolha
import insercao_selecao

def fazBuscaBin(lst, elem):
	inicio = 0
	fim = len(lst) - 1

	while inicio <= fim:
		meio = (inicio + fim)//2
		print(lst[meio])
		if lst[meio] == elem:
			inicio = fim + 1 # Provoca o fim do while
		elif lst[meio] > elem:
			fim = meio - 1
		else:
			inicio = meio + 1
		# fim else
	# fim while

	if lst[meio] == elem:
		return meio
	else:
		return -1
# fim fazBuscaBin

def main():
	lst = [12, 34, 67, 98, 21, 1, 5, 43]

	lst = insercao_direta.insertionSort(lst)[0]
	print(lst)

	print(fazBuscaBin(lst, 67))

# fim main

main()