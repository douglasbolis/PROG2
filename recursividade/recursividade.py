__author__ = 'douglas'

# (EXTRA)_Calcular a fatorial de um número N
def fatorial(n):
    def factInter(acc, x):
        if x == 0:
            return acc
        else:
            return factInter(acc*x, x-1)
        # fim else
    # fim factInter

    return factInter(1, n)
# fim fatorial

# (1)_Calcular a soma dos elementos de uma lista numérica.
def somaElem(lst):
    def somaInter(soma, xlst):
        if xlst == []:
            return soma
        else:
            return somaInter(soma + xlst[0], xlst[1:])
        # fim else
    # fim somaInter

    return somaInter(0, lst)
# fim somaElem

# (2)_permutações sobre um conjunto de n elementos
def permutacao(lst):
    def permConj(tupla, xlst):
        return 0
    # fim permConj

    return permConj((), lst)
# fim permutacao

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

    return encontraMaiorElem(0, lst)
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
    # Extra
    print(fatorial(100))

    # Exercício_1
    # lst = [12, 23, 34, 45, 56, 67, 78, 89, 90]
    # print(somaElem(lst))

    # Exercício_7
    # str = 'socorram-me, subi no onibus em marrocos'
    # print(inverteStr(str))

    # Exercício_9
    # lst = [12, 23, 34, 45, 546, 67, 8]
    # print(maiorElem(lst))

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