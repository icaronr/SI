#! python 
# -*- coding: utf-8 -*-
import getNews
import manipulador
import os

def scanfolder():
    lista = []
    #for path, dirs, files in os.walk('./'):
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if f.endswith('.xlsx'):
            lista.append(f)
    return lista
#lê uma planilha e devolve uma lista com os termos de busca
listaTermos = manipulador.carregaBusca()
# Faz uma busca para cada termo e retorna um json p cada
for termo in listaTermos:
    getNews.busca(termo)
# Transforma o json em xlsx
    manipulador.enchePlanilha(termo)
# faz a contagem de quantos xlsx tem na pasta
planilhas = scanfolder()
# faz o merge das planilhas
manipulador.mergePlanilhas(planilhas)

manipulador.limpaPasta()
