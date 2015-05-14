__author__ = 'douglas'

def separaPalavras(pTexto, strSep):
    auxSep = ''
    palSep = []

    for i in pTexto:
        if i not in strSep:
            auxSep += i
        elif auxSep:
            palSep.append(auxSep)
            auxSep = ''
        #fim else
    #fim for

    return palSep
#fim funcao

def main():
    strSeparadores = ' .,:;!?'
    texto = "Construa a função separaPal(<text>) que recebe como entrada um texto contendo um documento qualquer. " \
            "A Função deve retornar uma lista contendo as palavras presente no texto. " \
            "Uma palavra é uma sequencia de caracteres entre caracteres chamados de separadores."

    print(separaPalavras(texto, strSeparadores))
#fim main

if __name__ == "__main__":
    main()
#fim if