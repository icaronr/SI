#! python 
import pandas as pd 
import json
import xlwt

def carregaBusca():
    termos = pd.read_excel('source/termos.xlsx')
    print termos.columns

def enchePlanilha(termo):
    nomejson = termo +'.json'
    jason = json.loads(open(nomejson).read())
    print json.dumps(jason, indent=4, sort_keys=True)
    jayson = pd.DataFrame(jason['articles'])
    nomearquivo = termo + '.xlsx'
    jayson.to_excel('nomearquivo', index=False)
    
def mergePlanilhas(planilhas):
    excels = [pd.ExcelFile(name) for name in planilhas]
    frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]

    frames[1:] = [df[1:] for df in frames[1:]]

    combined = pd.concat(frames)

    combined.to_excel("saida.xlsx", header=False, index=False)