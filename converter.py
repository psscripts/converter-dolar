print('Seja Bem vindo')
while True:
	print('Conversao de moedas')
	rs = float(input('\033[33mSua quantidade de R$'))
	print('========================')
	cvdl = float(input('Qual a cotação do dolar? U$'))
	print('========================')
	cv = rs/cvdl
	print('========================')
	print(f'\033[35mA conversão é de R${cv}')