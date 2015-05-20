__author__ = 'douglas'

def main():
    lstStringLine, lstPosline = [], []

    arqRead = open('arqRead.txt', 'rt')

    pos = arqRead.tell()
    linha = arqRead.readline()

    while linha != '':
        lstStringLine.append(linha)
        lstPosline.append(pos)
        # repetindo para pegar os novos valores
        pos = arqRead.tell()
        linha = arqRead.readline()
    #fim while

    # arqRead.seek(lstPosline[2])
    # linha = arqRead.readline()
    # print(linha)

    # print("%100s - %s" %('Conteudo da linha', 'Numero da linha'))
    for i in range(len(lstPosline)):
        if (i%2 != 0):
            arqRead.seek(lstPosline[i])
            linha = arqRead.readline()
            print(linha[:-1] + " - " + str((i+1)))
        #fim if
    #fim

    arqRead.close()
#fim main

if __name__ == "__main__":
    main()
#fim if