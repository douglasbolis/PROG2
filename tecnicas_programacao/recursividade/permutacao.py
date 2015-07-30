__author__ = 'douglas'

def permutacao(lista):
	if len(lista) <= 1:
		return [lista]
	# fim if

	primeiro = lista[0]
	resto = lista[1:]
	resultado = []

	for perm in permutacao(resto):
		for i in range(len(perm)+1):
			resultado += [perm[:i]+[primeiro]+perm[i:]]
		# fim for
	# fim for

	return resultado
# fim permutacao

def main():
	print(permutacao([1, 2, 3]))
# fim main

main()