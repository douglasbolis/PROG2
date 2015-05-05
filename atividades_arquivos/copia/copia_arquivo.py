__author__ = "Douglas"

import sys

def cp(arqO, arqD):
	arquivoO = open(arqO, 'rt')
	arquivoD = open(arqD, 'wt')
	
	conteudoOrg = arquivoO.read()
	arquivoD.write(conteudoOrg)
	
	arquivoO.close()
	arquivoD.close()
	
	print("Copia realizada com sucesso.")
#fim cp

def main():
	if (len(sys.argv) == 3):
		cp(sys.argv[1], sys.argv[2])
	else:
		print("Quantidade de parametros incorreto\nUse: copia_arquivo.py <arquivo de origem> <arquivo de destino>")
	#fim else
	
	return 0
#fim main

if __name__ == '__main__':
	main()
#fim if
