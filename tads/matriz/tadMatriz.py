__author__ = 'douglas'


def criar(linhas, colunas):
    '''cria e retorna um TAD matriz de dimensões linhas, colunas dadas. Retorna
None se os valores de dimensões forem inválidas.'''

    if linhas < 1 or colunas < 1:
        return None
    else:
        return {"tam": [linhas, colunas]}
# fim funcao

def igual(TADMatrizA, TADMatrizB):
    '''retorna True se os TADMatrizes passados como argumento são iguais,
False caso contrário.'''

    return (TADMatrizA["tam"][0] == TADMatrizB["tam"][0]) and (TADMatrizA["tam"][1] == TADMatrizB["tam"][1])
# fim funcao

def multip(TADMatrizA, TADMatrizB):
    '''retorna a matriz produto das matrizes de entrada (tads). Retorna
None se as matrizes não puderem ser multiplicadas.'''

    matrizProd = {}




    return matrizProd
# fim funcao