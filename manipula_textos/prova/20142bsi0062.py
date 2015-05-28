__author__ = 'douglas'

import libplnP

def codec(lstTokens, lstArtigos, lstConj, lstPrepos):
	strCodificada = ''
	
	for tok in lstTokens:
		if tok in lstArtigos:
			strCodificada += 'a'
		elif tok in lstPrepos:
			strCodificada += 'p'
		elif tok in lstConj:
			strCodificada += 'c'
		elif tok.isdigit():
			strCodificada += 'N'
		elif tok[-1] in ['ª', 'º', '°']:
			strCodificada += 'O'
		elif tok[0].isupper():
			strCodificada += 'M'
		elif tok[0].islower():
			strCodificada += 'm'
		else:
			strCodificada += tok
		# fim else
	# fim for
		
	return strCodificada
# fim funcao

def carregaLst(nomeArq):
	lst = []
	try:
		arq = open(nomeArq, 'rt')
		linha = arq.readline()
		
		while linha != '':
			lst.append(linha.strip())
			linha = arq.readline()
		# fim while
		
		arq.close()
	except IOError:
		print("Arquivo '" + nomeArq + "' não existe.\n")
	# fim except
	
	return lst
# fim funcao

"""
		--- Construa a função tokenizadorN2 (<tokens>,<codificação>,<pronomes tratamento>) que recebe
		como parâmetros de entradas uma lista de toke, sua respectiva string codificada (saída da função da
		questão 1) e uma lista de pronomes de tratamento. A função tokenizadorN2 deve produzir como
		saída uma lista de tokens com 1 nível de abstração acima dos tokens de nível 1. Nesse novo nível de
		abstração são tratados como tokens as seguintes entidades de texto: pronomes de tratamento, datas,
		horas, palavras aglutinadas com aspas (como rod'agua e sat'anna) e citações. É obrigatório que a
		função deve fazer o seu trabalho atuando nos tokens de nível 1 a partir da string codificada
		correspondente, como analisado e desenvolvido nas aulas de laboratório.
		
		-- Exemplo do texto original, tokens de entrada (nível 1), string codificada e tokens de nível 2, saída
		da função pedida:
		
		-- (i) Texto original (aspas duplas não incluídas e apenas para conferência):
		"Amanha, Companhia Vale do Rio Doce roda d'agua: 'e assim foi' 1º V.Sra. V.Exma. 27/05/2015."
		
		-- (ii) ['Amanha', ',', ' ', 'Companhia', ' ', 'Vale', ' ', 'do', ' ', 'Rio', ' ', 'Doce', ' ', 'roda', ' ', 'd', "'", 'agua', ':', '
		', "'", 'e', ' ', 'assim', ' ', 'foi', "'", ' ', '1º', ' ', 'V', '.', 'Sra', '.', ' ', 'V', '.', 'Exma', '.', ' ','27', '/', '05', '/', '2015']
		
		-- (iii) 'M, m M p M M m m'm: 'm m m' O M.M. M.M. N/N/N.'
		
		-- (iii) ['Amanha', ',', ' ', 'Companhia', ' ', 'Vale', ' ', 'do', ' ', 'Rio', ' ', 'Doce', ' ', 'roda', ' ', “d''agua”, ':', ' ',
		"'e assim foi'", ' ', '1º', ' ', 'V.'Sra.', ' ', 'V.'Exma.', ' ', '27/05/2015']
"""

def tokenizadorN2(lstTokens, strCodificada, lstPronTratam):
	lstTokensN2 = []
	lstSepEnt = ['.', "'", ':', '/']
	strBuffer = ''
	
	for j in range(len(lstTokens)):
		if lstTokens[j] in lstSepEnt:
			pos = strCodificada.find(lstTokens[j])
			while pos > 0 and pos < len(strCodificada)-1:
				strBuffer = ''
				strCodificada = strCodificada.replace(lstTokens[j], '*', 1)
				
				if lstTokens[pos-1] != ' ' and lstTokens[pos+1] != ' ':
					i = pos-1
					while i < len(lstTokens) and lstTokens[i] != ' ':
						strBuffer += lstTokens[i]
						if lstTokens[i] == lstTokens[j]:
							strCodificada = strCodificada.replace(lstTokens[i], '*', 1)
						# fim if
						i += 1
					# fim while
					
					if strBuffer[-1] == ':':
						strBuffer = strBuffer[:-1]
					# fim if
					print(strBuffer)
					
				elif lstTokens[pos-1] == ' ':
					i = pos
					print(lstTokens[pos] + 'q')
					while lstTokens[i] != ' ' and i < len(lstTokens):
						if lstTokens[i] == lstTokens[j]:
							strCodificada = strCodificada.replace(lstTokens[j], '*', 1)
						# fim if
						strBuffer += lstTokens[i]
						i += 1
					# fim while
				# fim elif
				
				lstTokensN2.append(strBuffer)
				pos = strCodificada.find(lstTokens[j])
			# fim while
		else:
			if j+1 < len(lstTokens) and lstTokens[j+1] not in lstSepEnt:
				lstTokensN2.append(lstTokens[j])
			# fim if
	# fim for
	
	return lstTokensN2
# fim funcao

def main():
	#texto = input("Digite um texto para ser processado no tokenizador nivel 2: ")
	texto = "Amanha, Companhia Vale do Rio Doce roda d'agua: 'e assim foi' 1º V.Sra. V.Exma. 12/12/12"
	lstArtigos = carregaLst('artigos.txt')
	lstConj = carregaLst('conjuncoes.txt')
	lstPrepos = carregaLst('preposicoes.txt')
	lstPronTratam = carregaLst('prontratamento.txt')
	
	txtCod = codec(libplnP.tokenizador(texto), lstArtigos, lstConj, lstPrepos)
	lstTokensN2 = tokenizadorN2(libplnP.tokenizador(texto), txtCod, lstPronTratam)
	
	print(texto + '\n')
	print(lstTokensN2)
# fim main

if __name__ == "__main__":
	main()
# fim if














