# -*- coding: utf-8 -*-

from random import randint

#--------------------------------------------------
# FUNÇÃO DE CONCATENAÇÃO DE N LISTAS
#--------------------------------------------------
def concLst(*arg):
	conc = []
	indice = []         # Lista com o indice de cada lista passada como parâmetro
	argc = len(arg)     # Numero de listas passadas como parametro
	argl = 0            # Soma do tamanho de todas as listas
	i = 0; j = 0; imenor = 0; menor = 0;
	
	for elem in arg:
		argl += len(elem)
		indice.append(0) 
	
	while(i < argl):
		menor = float("inf")    # Pequeno belo recurso do python que atribui o valor "infinito"
		for j in range(argc):   # Roda o último índice usado por cada lista e procura o menor
			if(indice[j] < len(arg[j])):
				if(arg[j][indice[j]] < menor):
					menor = arg[j][indice[j]]
					imenor = j
				#---
			#---
		#---
		conc.append(menor)   # no fim de cada busca, salva o atual menor elemento
		indice[imenor] += 1  # e adiciona mais um no indice que foi usado
		i+=1
	
	return conc

#--------------------------------------------------
# SUB-ROTINAS AUXILIARES - NÃO NECESSÁRIAS PARA A CONCATENAÇÃO
#--------------------------------------------------

def fill_lst(n, vmin, vmax, *arg):
	for lst in arg:
		for i in range(n):
			lst.append(randint(vmin,vmax))
		#---
	#---
#---

def sortLst(*arg):
	for lst in arg:
		lst.sort()
	#---
#---

def printLst(lst):
	for elem in lst:
		print(elem)
	#---
#---

#--------------------------------------------------
# FUNÇÃO PRINCIPAL DE TESTES
#--------------------------------------------------
def teste1():
	lst1=[]; lst2=[]; lst3=[];
	fill_lst(5,0,100,lst1)
	fill_lst(9,0,100,lst2)
	fill_lst(8,0,100,lst3)
	sortLst(lst1,lst2,lst3)
	printLst([lst1,lst2,lst3])
	print("\nConcatenadas:")
	print(concLst(lst1,lst2,lst3))


def main():
	teste1()
	return 0

if __name__ == '__main__':
	main()
