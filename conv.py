from datetime import date
import requests
from json import loads
from time import sleep

try:
	from time import sleep
	import requests
except:

	print('Algo esta errado,digite o camando pip install -r requirements!')
	
pt=int(input('Deseja ver resultados da cotação? digite 1: '))

if pt == 1:
	
	print('\033[32mAtualizacoes a cada 10 segundos')

	while True:
		cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

		cotacoes_carregadas = loads(cotacoes.content)

		cotacoes_dolar = cotacoes_carregadas['USDBRL']['bid']

    	
		print('\033[35m---------------------------')
		sleep(10)
		data_real = date.today()
		print(data_real)
		
		print('\033[33mDolar para o Real >> R$' + cotacoes_dolar)
	
		cotacoesum =cotacoes_carregadas['EURBRL']['bid']
		print('Euro para o Real >> R$' + cotacoesum)
else:
	print('Volte sempre!')
	