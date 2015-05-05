__author__ = "Douglas"

import sys

def concat(lstArq):
    arqD = open(lstArq[len(lstArq)-1], 'wt')

    for arq in range(len(lstArq)-1):
        arqO = open(lstArq[arq], 'rt')

        arqD.write(arqO.read())

        arqO.close()
    #fim for

    arqD.close()

    print("Concatenacao realizada com sucesso.")
#fim concat

def main():
    # if (len(sys.argv) >= 3):
        #concat(sys.argv[1:])
    concat(['concat_1.txt', 'concat_2.txt', 'concat_3.txt', 'concat_destino.txt'])
    # else:
    #     print("\nQuantidade de parametros incorreto\nUse: python3 concatena_arquivos.py <arquivo 1> ... <arquivo N>\n\n")
    #fim else

    return 0
#fim main

if __name__ == '__main__':
    main()
#fim if
