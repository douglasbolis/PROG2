__author__ = 'douglas'


def criar(linhas, colunas):
    '''cria e retorna um TAD matriz de dimensões linhas, colunas dadas. Retorna
None se os valores de dimensões forem inválidas.'''

    if linhas < 1 or colunas < 1:
        return None
    else:
        return {"lin": linhas, "col": colunas}
# fim funcao

def igual(TADMatrizA, TADMatrizB):
    '''retorna True se os TADMatrizes passados como argumento são iguais,
False caso contrário.'''

    return (TADMatrizA["lin"] == TADMatrizB["lin"]) and (TADMatrizA["col"] == TADMatrizB["col"])
# fim funcao

def multip(TADMatrizA, TADMatrizB):
    '''retorna a matriz produto das matrizes de entrada (tads). Retorna
None se as matrizes não puderem ser multiplicadas.'''

    matrizProd = criar(TADMatrizA["lin"], TADMatrizA["col"])

    if TADMatrizA["lin"] == TADMatrizB["col"]:
        for i in range(TADMatrizA["lin"]):
            for j in range(TADMatrizB["col"]):
                acc = 0
                for k in range(TADMatrizA["col"]):
                    posMatrizA = str(i) + str(k)
                    posMatrizB = str(k) + str(j)

                    acc += TADMatrizA[posMatrizA] * TADMatrizB[posMatrizB]
                # fim for
                adElem(matrizProd, acc, i, j)
            # fim for
        # fim for
    # fim if

    return matrizProd
# fim funcao

def adElem(TADMatriz, elem, i, j):
    '''altera a matriz de entrada adicionando o elemento na posição i, j do
tadmatriz. Caso i, j sejam posições invaálidas, retornar None. Retornar a matriz em caso de sucesso.'''

    if elem != 0:
        pos = str(i) + str(j)
        TADMatriz[pos] = elem
    # fim if
# fim funcao

def main():
    matrizA = criar(2, 2)
    matrizB = criar(2, 2)

    adElem(matrizA, 1, 0, 0)
    adElem(matrizA, 2, 0, 1)
    adElem(matrizA, 3, 1, 0)
    adElem(matrizA, 4, 1, 1)

    adElem(matrizB, 5, 0, 0)
    adElem(matrizB, 6, 0, 1)
    adElem(matrizB, 7, 1, 0)
    adElem(matrizB, 8, 1, 1)

    matrizC = multip(matrizA, matrizB)

    print("\nMatriz C: ", end="")
    print(matrizC)

# fim main

main()