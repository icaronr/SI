import requests
import datetime


now = datetime.datetime.now()

date = (str(now.year) + '-' +
'{:02d}'.format(now.month) + '-' +
'{:02d}'.format(now.day -1))

print(date)
url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from='+ date + '&'
       'sortBy=relevance&'
       'domains=Jb.com.br, globo.com, uol.com.br&'
       'apiKey=96aa6314cd3843ada8414cd9163549a7')

print(url)
response = requests.get(url)

print response.json()

#Salvar o json em uma planilha excel .xlsx
#melhor alternativa para nao utilizar um bd

#carregar o excel para a memoria, um dicionario, por ser python(hashtable)

#carregar os parametros de classificacao

#rodar o algoritmo de classificacao e gerar uma nova tabela que vai conter as noticias ordenadas
#alternativa: sobrescrever a primeira planilha
