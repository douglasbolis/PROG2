__author__ = "Douglas"

import sys

def rvAcentos(arqO, arqD):
	dicAcentos = {
		"Á": "A", "Â": "A", "Ã": "A", "À": "A", "Ä": "A",
		"á": "a", "â": "a", "ã": "a", "à": "a", "ä": "a",
		"É": "E", "Ê": "E", "Ẽ": "E", "È": "E", "Ë": "E",
		"é": "e", "ê": "e", "ẽ": "e", "è": "e", "ë": "e",
		"Í": "I", "Î": "I", "Ĩ": "I", "Ì": "I", "Ï": "I",
		"í": "i", "î": "i", "ĩ": "i", "ì": "i", "ï": "i",
		"Ó": "O", "Ô": "O", "Õ": "O", "Ò": "O", "Ö": "O",
		"ó": "o", "ô": "o", "õ": "o", "ò": "o", "ö": "o",
		"Ú": "u", "Û": "u", "Ũ": "u", "Ù": "u", "Ü": "u",
		"ú": "u", "û": "u", "ũ": "u", "ù": "u", "ü": "u",
		}
	arquivoO = open(arqO, 'rt')
	arquivoD = open(arqD, 'wt')

	contOrig = arquivoO.read()
	contDest = ''

	for elem in range(len(contOrig)-1):
		if contOrig[elem] in dicAcentos:
			contDest += str(dicAcentos[contOrig[elem]])
		else:
			contDest += contOrig[elem]
		#fim else
	#fim for

	arquivoD.write(contDest)

	arquivoO.close()
	arquivoD.close()

	print("Remocao dos acentos realizada com sucesso.")
#fim cp

def main():
	# if (len(sys.argv) == 3):
	# 	rvAcentos(sys.argv[1], sys.argv[2])
	rvAcentos('sem_acentos_origem.txt', 'sem_acentos_destino.txt')
	# else:
	# 	print("Quantidade de parametros incorreto\nUse: sem_acentos.py <arquivo de origem> <arquivo de destino>")
	#fim else
	
	return 0
#fim main

if __name__ == '__main__':
	main()
#fim if
