__author__ = 'Douglas'

_caracteresCifra = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ,.;:'

def cifraCesar(mensagem, ndesloc):
	textoCifra = ''
	mensagem = mensagem.upper()

	for ch in mensagem:
		if ch == ' ':
			textoCifra += '*'
		elif ch in _caracteresCifra:
			idx = _caracteresCifra.find(ch) + ndesloc

			if idx >= 30:
				idx -= 30
			# fim if
			textoCifra += _caracteresCifra[idx]
		# fim if
	# fim for

	return textoCifra
# fim cifraCesar

def decifraCesar(textoCifrado,  ndesloc):
	textoDecifra = ''
	textoCifrado = textoCifrado.upper()

	for ch in textoCifrado:
		if ch == '*':
			textoDecifra += ' '
		elif ch in _caracteresCifra:
			idx = _caracteresCifra.find(ch) - ndesloc
			textoDecifra += _caracteresCifra[idx]
		# fim if
	# fim for

	return textoDecifra.lower()
# fim decifraCesar

def main():
	texto = 'Aula de matematica: Dia nove'
	desloc = 3

	textoCifrado = cifraCesar(texto, desloc)

	print(textoCifrado)

	textoDecifrado = decifraCesar(textoCifrado, desloc)

	print(textoDecifrado)
# fim main

main()