__author__ = 'douglas'

import libplnbsi

def main():
    texto = open('concat_1.txt', 'rt')
    strSep = " "
    libplnbsi.tabFreg(texto.read(), strSep)
#fim main

main()