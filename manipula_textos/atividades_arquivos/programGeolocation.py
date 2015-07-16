__author__ = 'douglas'

#-  PARAMETROS(*)   arquivo de origem, arquivo destino, separador, lista de indices, codificacao    -#
def geraIndexa(arqOrig, arqDest, sep, lstIndex, encoded):
    arqGeoLocRead = open(arqOrig, 'rt', encoding=encoded)
    arqGeoLocWrite = open(arqDest, 'wt')

    pos = arqGeoLocRead.tell()
    linha = arqGeoLocRead.readline()

    while linha != '':
        geolocFullLine = tuplaIndex(linha, sep, lstIndex)
        arqGeoLocWrite.write(str(geolocFullLine) + "," + str(pos) + "\n")
        # repetindo para pegar os novos valores
        pos = arqGeoLocRead.tell()
        linha = arqGeoLocRead.readline()
    #fim while

    arqGeoLocWrite.close()
    arqGeoLocRead.close()
#fim main

def tuplaIndex(line, sep, lstIndex):
    line = line.split(sep)
    lst = []

    for i in lstIndex:
        lst.append(line[i])
    #fim for

    return tuple(lst)
# fim funcao

def main():
#-  PARAMETROS(*)   arquivo de origem, arquivo destino, separador, lista de indices, codificacao    -#
    # geraIndexa('arqOrigMan/bibliotecas_geo5.csv', 'arqDestMan/geolocations.ndx', '|', [1, 2], 'latin2')
    # geraIndexa('arqOrigMan/consulta_cand_2012_ES.txt', 'arqDestMan/consCandES2012.ndx', ';', [11], 'latin1')
    geraIndexa('arqOrigMan/teste_funcao.txt', 'arqDestMan/teste_funcao.ndx', ',', [0, 1], 'utf-8')

#fim main

if __name__ == "__main__":
    main()
#fim if