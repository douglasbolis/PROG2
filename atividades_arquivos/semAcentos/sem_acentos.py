__author__ = "Douglas"

import sys

def rvAcentos(arqO, arqD):
	dicAcentos = {
		"A": "ÁÂÃÀÄ",
		"a": "áâãàä",
		"E": "ÉÊẼÈË",
		"e": "éêẽèë",
		"I": "ÍÎĨÌÏ",
		"i": "íîĩìï",
		"O": "ÓÔÕÒÖ",
		"o": "óôõòö",
		"U": "ÚÛŨÙÜ",
		"u": "úûũùü"
	}
	arquivoO = open(arqO, 'rt')
	arquivoD = open(arqD, 'wt')

	conteudoOrg = arquivoO.read()

	for ltr in conteudoOrg:
		if ltr in dicAcentos:
			arquivoD.write(conteudoOrg)
		#fim if
	#fim for

	arquivoO.close()
	arquivoD.close()

	print("Remocao dos acentos realizada com sucesso.")
#fim cp

def main():
	if (len(sys.argv) == 3):
		rvAcentos(sys.argv[1], sys.argv[2])
	else:
		print("Quantidade de parametros incorreto\nUse: sem_acentos.py <arquivo de origem> <arquivo de destino>")
	#fim else
	
	return 0
#fim main

if __name__ == '__main__':
	main()
#fim if
