__author__ = 'douglas'

def nGrama(pTexto, pTam):
    lst = []

    for i in range((len(pTexto) - pTam) + 1):
        lst.append(pTexto[i:i+pTam])
    #fim for
    return lst
#fim funcao

def main():
    texto = "estudo"
    tam = 2

    print(nGrama(texto, tam))
#fim main

if __name__ == "__main__":
    main()
#fim if