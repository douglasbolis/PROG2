__author__ = 'Douglas'

'''
A função cifraCesar(<mensagem>,<ndesloc>) retorna criptografada a mensagem passada como
parâmetro de entrada com deslocamento passado como segundo parâmetro.
Ex.: 'Aula de matemática: Capítulo nove'
Ret.: 'DXOD*GH*PDWHPÄWLFD=*FDSÐWXOR*QRYH'
'''
def cifraCesar(mensagem, ndesloc):
	textoCifra = ''
	mensagem = mensagem.upper()

	for ch in mensagem:
		if ch == ' ':
			textoCifra += '*'
		else:
			textoCifra += chr(ord(ch) + ndesloc)
		# fim if
	# fim for

	return textoCifra
# fim cifraCesar

'''
A função decifraCesar(<mensagem>,<ndesloc>) retorna descriptografada  a mensagem passada como
parâmetro de entrada com deslocamento passado como segundo parâmetro.
Ex.: 'DXOD*GH*PDWHPÄWLFD=*FDSÐWXOR*QRYH'
Ret.: 'Aula de matemática: Capítulo nove'
'''
def decifraCesar(textoCifrado,  ndesloc):
	textoDecifra = ''
	textoCifrado = textoCifrado.upper()

	for ch in textoCifrado:
		if ch == '*':
			textoDecifra += ' '
		else:
			textoDecifra += chr(ord(ch) - ndesloc)
		# fim if
	# fim for

	return textoDecifra.lower()
# fim decifraCesar

def cifraEspartana(mensagem):

	return mensagem
# fim cifraEspartana

def decifraEspartana(mensagem):

	return mensagem
# fim decifraEspartana

def criptografa(mensagem):
	desloc = 13

	return cifraEspartana(cifraCesar(mensagem, desloc))
# fim criptografa

def descriptografa(mensagem):
	desloc = 13

	return decifraEspartana(decifraCesar(mensagem, desloc))
# fim descriptorgafa

def main():
	arqRead = open('cripto.txt', 'rt')

	linha = arqRead.readline()

	while linha != '':
		print(descriptografa(criptografa(descriptografa(linha.strip()))))
		linha = arqRead.readline()
	# fim while

	arqRead.close()
# fim main

main()