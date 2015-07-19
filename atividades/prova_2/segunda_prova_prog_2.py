__author__ = 'Douglas'

#~ Email: douglasbolislima@gmai.com

import tadcomplex
import tadmatrix

# QUESTÃO (1)(a)
def indexabd(paramNomeArq):
	arqLeitura = open(paramNomeArq + '.txt', 'rt')
	arqEscrita = open(paramNomeArq + '.ndx', 'wt')
	
	posCursor = arqLeitura.tell()
	linhaArqLeitura = arqLeitura.readline()
	
	while linhaArqLeitura != '':
		if (linhaArqLeitura.find(',') != -1):
			lstLinhaArqLeitura = linhaArqLeitura.strip().split(', ')			
			arqEscrita.write(lstLinhaArqLeitura[0] + ', ' + str(posCursor) + '\n')	
		# fim if
		
		posCursor = arqLeitura.tell()
		linhaArqLeitura = arqLeitura.readline()
	# fim while
		
	arqEscrita.close()
	arqLeitura.close()
# fim funcao

def carregaIndices(paramNomeArqDados):
	dicDados = {}
	arqLeituraDados = open(paramNomeArqDados + '.txt', 'rt')
	arqLeituraIdx = open(paramNomeArqDados + '.ndx', 'rt')
	
	linhaArqLeituraIdx = arqLeituraIdx.readline()
	
	while linhaArqLeituraIdx != '':
		lstLinhaArqLeituraIdx = linhaArqLeituraIdx.strip().split(', ')
		
		arqLeituraDados.seek(int(lstLinhaArqLeituraIdx[1]))

		linhaArqLeituraDados = arqLeituraDados.readline()
		
		lstLinhaArqLeituraDados = linhaArqLeituraDados.strip().split(', ')
		dicDados[lstLinhaArqLeituraIdx[0]] = []
		
		for i in range(int(lstLinhaArqLeituraDados[1])):
			lstTempDados = []	
			linhaArqLeituraDados = arqLeituraDados.readline()			
			lstLinhaArqLeituraDados = linhaArqLeituraDados.strip().split('  ')
			
			for el in lstLinhaArqLeituraDados:
				lstTempDados.append(el)
			# fim for
			dicDados[lstLinhaArqLeituraIdx[0]].append(lstTempDados)
		# fim for		

		linhaArqLeituraIdx = arqLeituraIdx.readline()
	# fim while
		
	arqLeituraIdx.close()
	arqLeituraDados.close()
	
	return dicDados
# fim funcao

def main():
	# dic = {}
	#
	# indexabd('bd-mat-complex')
	# dic = carregaIndices('bd-mat-complex')
	# print(dic['A'])

	print(tadcomplex.criaStr('-4.5-5.25i'))
# fim main

main()
