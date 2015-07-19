#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  libplnP.py
#  
#  Biblioteca pln para a prova de prog2.
#
#  Copyright 2015 Ernani Ribeiro Fo <ernani@HAL>
#  

def tokenizador(paramtxt):
	lstresult = []	
	strbuffer = ''
	
	citando = False
	inicio, fim = 0, 0
	
	for pos, elem in enumerate(paramtxt):
		# Se for um caracter alfanumerico.
		if elem.isalnum(): 
			strbuffer += elem
		else:
			if strbuffer != '':
				lstresult.append(strbuffer)
				strbuffer = ''
				
			if elem == ' ': # inclui espaco como token. 
				# sequencias de espaçoes seguidos são incluidos como apenas um token
				# espaco.
				if (pos > 0) and (paramtxt[pos-1] != ' '):	
					lstresult.append(elem)
			else:
				lstresult.append(elem)
	
	if strbuffer != '':
		lstresult.append(strbuffer)
	
	return lstresult	
# fim tokenizador


def main():
	txt = "Amanha,  Companhia   Vale do   Rio   Doce  roda d'agua: 'e assim foi' 1º V.Sra. V.Exma. 27/05/2015"
	
	print(txt)
	print(tokenizador(txt))
	
	return 0

if __name__ == '__main__':
	main()

