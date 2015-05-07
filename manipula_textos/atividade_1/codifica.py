__author__ = "Douglas"

def codifica(pLst):
	lstArtigos = ['a', 'as', 'o', 'os', 'um', 'uma', 'umas', 'uns']
	lstConj = ['e', 'nem', 'mas também', 'como também', 'bem', 'como', 'mas', 'porém', 'todavia', 'contudo', 'entretanto', 'no entanto', 'logo', 'portanto', 'por isso', 'assim', 'por seguinte', 'que', 'porque', 'porquanto', 'pois']
	lstPrepos = ['a', 'ante', 'até', 'após', 'de', 'desde', 'em', 'entre', 'com', 'contra', 'para', 'pro', 'perante', 'sem', 'sob', 'sobre', 'como', 'conforme', 'segundo', 'durante', 'fora', 'exceto']
	strCodif = ''	
	
	for lstAux in pLst:
		if (lstAux.isalpha()):
			if (lstAux in lstArtigos):
				strCodif += 'a'
			elif (lstAux in lstConj):
				strCodif += 'c'
			elif (lstAux in lstPrepos):
				strCodif += 'p'
			elif (lstAux[0].isupper()):
				strCodif += 'M'
			elif (lstAux[0].islower()):
				strCodif += 'm'
		elif (lstAux.isdigit()):
			strCodif += 'N'
		else:
			strCodif += lstAux
		#fim else
	#fim for
	
	return strCodif
#fim funcao

def main():
	lstTokens = ['Semana', 'passada', 'eu', 'toquei', 'no', 'assunto', 'do', 'módulo', 'Progress', ',', 'destinado', 'a', 'levar', 'suprimentos', 'para', 'a', 'Estação', 'Espacial', 'Internacional', ',', 'ISS', 'em', 'inglês', ',', 'que', 'falhou', 'assim', 'que', 'foi', 'colocada', 'em', 'órbita', '.', 'Mas', 'relembrando', 'os', 'fatos', ',', 'foi', 'assim', '.']
	
	strCodifica = codifica(lstTokens)
	print(strCodifica)
	
	return 0
#fim main

if __name__ == '__main__':
	main()
#fim if
