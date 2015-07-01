__author__ = 'douglas'

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  TAD_RETANGULO.py
#
#  Autor: Danilo de Oliveira
#  Criado em: 24/06/15 15:57:06
#  Usuário: 20142bsi0186
#
#  Função do programa: APLICAÇÃO DO TAD_RETANGULO FAZENDO USO DA BIBIOTECA GRÁFICA (TKINTER).
#  Versão inicial: 1.0
#  ----------------------------------------------------------------


from TAD_RETANGULO import *
import time
import tkinter

def MovimentR(retangle,canvas,dx,dy,cor):
    # Apaga o retangulo
    canvas.create_rectangle(retangle,fill="white",outline="white")
    # Move-se dx unidades a direita e dy unidades a esquerda.
    move(retangle,dx,dy)
    # Desenha o retangul,o movido.
    canvas.create_rectangle(retangle,fill=cor)
    # Update mostra o resultado na tela de trabalho ("Janelinha").

    return None


def main():
    # Retangulo1
    R1 = criarVtx(0,0,200,100)

    # Retangulo2
    R2 = criarVtx(0,0,100,200)

    # Cria a raiz da "janelinha".
    raiz = tkinter.Tk()

    # Variaveis que irão deslocar o retangulo n pixels.
    dx = 3
    dy = 5

    da = 2
    db = 2

    canvas = tkinter.Canvas(raiz,width="600",height="500",bg="white")
    canvas.pack()


    while True:
        MovimentR(R2,canvas,dx,dy,'blue')
        MovimentR(R1,canvas,da,db,'yellow')

        inte = intersec(R1,R2)
        inte2 = intersec(R2,R1)

        if inte != None:
            canvas.create_rectangle(inte,fill="red")

        elif inte2!=None:
            canvas.create_rectangle(inte2,fill="red")
        canvas.update()

        time.sleep(0.01)


        if R1[1][0] > 598 or R1[0][0] < 2:
            da *= -1
        if R1[0][1] < 2 or R1[1][1] > 498:
            db *= -1

        if R2[1][0] > 598 or R2[0][0] < 2:
            dx *= -1
        if R2[0][1] < 2 or R2[1][1] > 498:
            dy *= -1


    raiz.mainloop()

    return 0

if __name__ == '__main__':
    main()
