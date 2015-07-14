__author__ = 'douglas'

'''     Atividades Extras     '''

# (EXTRA_1)_Calcular a fatorial de um número N
def fatorial(n):
    def factIter(acc, x):
        if x == 0:
            return acc
        else:
            return factIter(acc*x, x-1)
        # fim else
    # fim factIter

    return factIter(1, n)
# fim fatorial

'''     Atividades da Lista     '''

# (1)_Calcular a soma dos elementos de uma lista numérica.
def somaElem(lst):
    def somaIter(soma, xlst):
        if xlst == []:
            return soma
        else:
            return somaIter(soma + xlst[0], xlst[1:])
        # fim else
    # fim somaIter

    return somaIter(0, lst)
# fim somaElem

# (2)_permutações sobre um conjunto de n elementos
def permutacao(lst):
    def permConj(tupla, xlst):
        return 0
    # fim permConj

    return permConj((), lst)
# fim permutacao

# (5)_Calcula a raiz quadrada de um número n com tolerância máxima t.
def sqrt(n, t):
    def sqrtIter(aux, x):
        if ehBomSuficiente(aux, x):
            return aux
        else:
            return sqrtIter(melhoraResult(aux, x), x)
            # fim else
    # fim sqrtIter

    def melhoraResult(param_aux, param_x):
        return (param_aux + param_x / param_aux) / 2
    # fim melhoraResult

    def ehBomSuficiente(param_aux, param_x):
        return abs((param_aux**2) - param_x) < t
    # fim ehBomSuficiente

    return sqrtIter(1.0, n)
# fim fatorial

# (7)_Inverter uma string de entrada.
def inverteStr(str):
    def invStr(novaStr, xstr):
        if xstr == '':
            return novaStr
        else:
            return invStr(xstr[0] + novaStr, xstr[1:])
    # fim invStr

    return invStr('', str)
# fim inverteStr

# (8)_Testar se um número n passado como parâmetro é um número natural.
def ehNatural(n, incZero):
    def verificaNum(param_n, param_limInf):
        if param_n < param_limInf:
            return False
        elif param_n == param_limInf:
            return True
        else:
            return verificaNum(param_n-1, param_limInf)
    # verificaNum

    if incZero:
        return verificaNum(n, 0)
    else:
        return verificaNum(n, 1)
    # fim else
# fim ehNatural

# (9)_Calcular o maior valor de uma lista de números fornecida como entrada.
def maiorElem(lst):
    def encontraMaiorElem(maior, xlst):
        if xlst == []:
            return maior
        elif maior < xlst[0]:
            return encontraMaiorElem(xlst[0], xlst[1:])
        else:
            return encontraMaiorElem(maior, xlst[1:])
        # fim else
    # fim encontraMaiorElem

    return encontraMaiorElem(-1*fatorial(100), lst)
# fim maiorElem

# (10)_Calcular o menor valor de uma lista de números fornecida como entrad
def menorElem(lst):
    def encontraMenorElem(menor, xlst):
        if xlst == []:
            return menor
        elif menor > xlst[0]:
            return encontraMenorElem(xlst[0], xlst[1:])
        else:
            return encontraMenorElem(menor, xlst[1:])
            # fim else
    # fim encontraMaiorElem

    return encontraMenorElem(fatorial(100), lst)
# fim maiorElem

# (11)_Testar se uma string de entrada é um palíndromo. Retorna True caso seja, False caso não seja um palíndromo.
def ehPalindromo(str):
    strSep = encontraSeparedores(str)
    str = removeSeparadores(str, strSep)

    strAux = inverteStr(str)

    return str == strAux
# fim ehPalindromo

# (11)_Auxiliar do exercício 11
def encontraSeparedores(str):
    def procuraSep(sep, xstr):
        if xstr == '':
            return sep
        elif xstr[0].isalnum():
            return procuraSep(sep, xstr[1:])
        elif xstr[0] in sep:
            return procuraSep(sep, xstr[1:])
        else:
            return procuraSep(sep + xstr[0], xstr[1:])
    # fim procuraSep

    return procuraSep('', str)
# fim encontraSeparedores

# (11)_Auxiliar do exercício 11
def removeSeparadores(str, strSep):
    def rmSep(novaStr, xstr):
        if xstr == '':
            return novaStr
        elif xstr[0] in strSep:
            return rmSep(novaStr, xstr[1:])
        else:
            return rmSep(novaStr + xstr[0], xstr[1:])
    # fim rmSep

    return rmSep('', str)
# fim removeSeparadores

def main():
    # Extra_1
    # print(fatorial(100))

    # Exercício_1
    # lst = [12, 23, 34, 45, 56, 67, 78, 89, 90]
    # print(somaElem(lst))

    # Exercício_5
    # print(sqrt(4, 0.0001))

    # Exercício_7
    # str = 'socorram-me, subi no onibus em marrocos'
    # print(inverteStr(str))

    # Exercício_8
    # print(ehNatural(7, False))
    # print(ehNatural(0, True))
    # print(ehNatural(0, False))
    # print(ehNatural(-8, False))
    # print(ehNatural(2.5, False))

    # Exercício_9
    lst = [12, 23, 34, 45, 546, 67, 8]
    lst2 = []
    print(maiorElem(lst2))

    # Exercício_10
    # lst = [12, 23, 34, 45, 546, 67, 8]
    # print(menorElem(lst))

    # Exercício_11
    # str = 'socorram-me, subi no onibus em marrocos'
    # str2 = 'oto come mocoto'
    # str3 = 'amanha é marrocos'
    # print(ehPalindromo(str3))
# fim main

main()