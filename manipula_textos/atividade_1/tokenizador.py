__author__ = "Douglas"

def tokenizador(pTexto):
	strSep = [' ', '.', ',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '\\', '|', '/', '\n', '\t', '"'];
	lstTokens, lstPosicoes = [], []
	strBuffer, pos = '', 0
	
	while pos < len(pTexto):
		if (pTexto[pos] not in strSep):
			strBuffer += pTexto[pos]
		else:
			if (strBuffer != ''):
				lstTokens.append(strBuffer)
				lstPosicoes.append(pos-len(strBuffer))
				strBuffer = ''
			#fim if
			
			if (pTexto[pos] not in [' ', '\t']):
				lstTokens.append(pTexto[pos])
				lstPosicoes.append(pos)
			#fim if
		#fim else
		pos += 1	
	#fim while
	
	if strBuffer != '':
		lstTokens.append(strBuffer)
		lstPosicoes.append(pos-len(strBuffer))
	#fim if	
	
	return lstTokens, lstPosicoes
#fim funcao

def main():
	texto = "Semana passada (22/12/2014) eu toquei no assunto do módulo Progress, destinado a levar suprimentos para a Estação Espacial Internacional, ISS em inglês, que falhou assim que foi colocada em órbita. Mas relembrando os fatos, foi assim."
	
	lstTokens, lstPos = tokenizador(texto)
	
	print(lstTokens)
	print(lstPos)
	
	return 0
#fim main

if __name__ == '__main__':
	main()
#fim if
