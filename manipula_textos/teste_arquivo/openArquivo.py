__author__ = 'douglas'

def main():
    arqOpen = 'teste3.txt'
    try:
        a = [1, 2]
        print(a[1] + '1')
    except IndexError:
        print('Indice fora do range')
    except TypeError:
        print('tipo errado')
    # try:
    #     arq = open(arqOpen, 'rt')
    #     arq.close()
    #
    #     print('O arquivo já existe')
    # except IOError:
    #     print('Arquivo não existe')
    #
    #     arq = open(arqOpen, 'wt')
    #     arq.write("(123,456),123456")
    #     arq.close()
    # fim else
# fim main

main()