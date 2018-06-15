#! python 
import pandas as pd 
import json
import xlwt
import xlsxwriter
import os

def carregaBusca():
    termos = pd.read_excel('source/termos.xlsx')
    listaTermos = termos['Nome'].tolist()
    return listaTermos

def enchePlanilha(termo):
    nomejson = termo + '.json'
    print nomejson
    
    jason = json.loads(open(nomejson).read())
    #print json.dumps(jason, indent=4, sort_keys=True)
    print "JSON CARREGADO"
    jayson = pd.DataFrame(jason['articles'])
    numcolunas = jayson.shape[0]
    print numcolunas
    nomedoenca = []
    for x in range(0, numcolunas):
        nomedoenca.append(termo)
    jayson['Nome Doenca'] = nomedoenca
    nomearquivo = termo + '.xlsx'
    writer = pd.ExcelWriter(nomearquivo)
    jayson.to_excel(writer,'Sheet1')
    #jayson.to_excel('nomearquivo', index=False, engine='openpyxl')
    

    
def mergePlanilhas(planilhas):
    excels = [pd.ExcelFile(name) for name in planilhas]
    frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]

    frames[1:] = [df[1:] for df in frames[1:]]

    combined = pd.concat(frames)

    combined.to_excel("saida/saida.xlsx", header=False, index=False)

def limpaPasta():
    for name in os.listdir("."):
        if name.endswith(".xlsx"):
            os.remove(name)
        if name.endswith(".json"):
            os.remove(name)


carregaBusca()