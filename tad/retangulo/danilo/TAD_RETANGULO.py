__author__ = 'douglas'

def criarVtx(xsEsq,ysEsq,xiDir,yiDir):
    return [[xsEsq,ysEsq],[xiDir,yiDir]]

def criarDim(xsEsq,ysEsq,larg,alt):
    return [[xsEsq,ysEsq],[xsEsq+larg,ysEsq+alt]]


# Função que retorna os cantos superior direito e inferior esquerdo.
def getCantos(param_retangulo):
    return param_retangulo


# Retorna o canto Superior Esquerdo
def getCantoSE(retang):
    return retang[0]


# Retorna o canto Superior Direito
def getCantoSD(retang):
    return [retang[1][0],retang[0][1]]


# Retorna o canto Inferior Esquerdo
def getCantoIE(retang):
    return [retang[0][0],retang[1][1]]

# Retorna o canto Inferior Direito
def getCantoID(retang):
    return retang[1]



# # Retorna o perímetro do retangulo
def perimetro(param_retangulo):
    return float((param_retangulo[1][0]-param_retangulo[0][0])*2+(param_retangulo[1][1]-param_retangulo[0][1])*2)


# Retorna a área do retangulo.
def area(param_retang):
    return (param_retangulo[1][0]-param_retangulo[0][0])*(param_retangulo[1][1]-param_retangulo[0][1])



# Retorna True se os retangulos forem iguais e False senão.
def igual(param_retang1,param_retang2):
    if (param_retang1[1][0]-param_retang1[0][0]) == (param_retang2[1][0]-param_retang2[0][0]):
        return (param_retang1[1][1]-param_retang1[0][1]) == (param_retang2[1][1]-param_retang2[0][1])

    else:
        return False


# Modificador. Desloca o retangulo dx unidades para esquerda ou direita e dy unidades para cima ou para baixo.
def move(param_retangulo,dx,dy):
    param_retangulo[0][0]+=dx
    param_retangulo[0][1]+=dy
    param_retangulo[1][0]+=dx
    param_retangulo[1][1]+=dy

    return 0


# Função interna do TAD que verifica se o ponto dado está dentro do retangulo.
def _VInterior(retangA,ponto):
    retan_result= []
    x = retangA[0][0]
    y = retangA[0][1]
    a = retangA[1][0]
    b = retangA[1][1]

    c = ponto[0]
    d = ponto[1]


    if (x < c) and (c < a) and (y < d) and (d < b):
        return True
    else:
        return False

# Essa função é a melhor e a que deu mais trabalho. Ela retorna o RETANGULO INTERSECÇÃO entre dois retangulos ou None se não existir.
def intersec(retang1,retang2):
    c_SD = getCantoSD(retang2)
    c_SE = getCantoSE(retang2)
    c_ID = getCantoID(retang2)
    c_IE = getCantoIE(retang2)


    SD = _VInterior(retang1,c_SD)
    SE = _VInterior(retang1,c_SE)
    ID = _VInterior(retang1,c_ID)
    IE = _VInterior(retang1,c_IE)


    if SD and SE and ID and IE:
        return retang2

    elif SD and SE:
        return [c_SE,[c_ID[0],retang1[1][1]]]

    elif SD and ID:
        return [[retang1[0][0],c_SE[1]],c_ID]

    elif ID and IE:
        return [[c_IE[0],retang1[0][1]],c_ID]

    elif SE and IE:
        return [c_SE,[retang1[1][0],c_IE[1]]]

    elif ID:
        return [c_ID,retang1[0]]
    elif IE:
        return [c_IE,getCantoSD(retang1)]
    elif SE:
        return [c_SE,retang1[1]]
    elif SD:
        return [c_SD,getCantoIE(retang1)]
    else:
        return None

def main():
    return 0

if __name__=='__main__':
    main()
