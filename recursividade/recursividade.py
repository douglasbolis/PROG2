__author__ = 'douglas'

# Calcular a soma dos elementos de uma lista numérica.
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

def ehPalindromo(str):
    strSep = encontraSeparedores(str)
    str = removeSeparadores(str, strSep)

    strAux = inverteStr(str)

    return str == strAux
# fim ehPalindromo

def inverteStr(str):
    def invStr(novaStr, xstr):
        if xstr == '':
            return novaStr
        else:
            return invStr(xstr[0] + novaStr, xstr[1:])
    # fim invStr

    return invStr('', str)
# fim inverteStr

def encontraSeparedores(str):
    def procuraSep(sep, xstr):
        if xstr == '':
            return sep
        elif xstr[0].isalnum():
            return procuraSep(sep, xstr[1:])
        else:

            return procuraSep(sep + xstr[0], xstr[1:])
    # fim procuraSep

    return procuraSep('', str)
# fim encontraSeparedores

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
    # Exercício_1
    # lst = [12, 23, 34, 45, 56, 67, 78, 89, 90]
    # print(somaElem(lst))

    # Exercício_11
    str = 'socorram-me, subi no onibus em marrocos'
    str2 = 'oto come mocoto'
    str3 = 'amanha é marrocos'
    print(ehPalindromo(str3))
# fim main

main()