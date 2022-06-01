#Jonathan Santiago Marques, Polo: Itaguai, Mat: 20213050125
# AP2X - Questão 1

import os.path

nome_arquivo = 'Delta.txt'
def procurar_arquivo():
		if os.path.exists(nome_arquivo):
			return open(nome_arquivo,'r',encoding='utf-8').read().strip()


def ordenar(matriz):
	for loop_1 in range(len(matriz)-1):
		for loop_2 in range(len(matriz)-1-loop_1):
			if (matriz[loop_2] > matriz[loop_2+1]):
				matriz[loop_2] ,matriz[loop_2+1] = matriz[loop_2+1] , matriz[loop_2]

	matriz_new = ''
	for i in matriz:
		matriz_new += str(i) + ' '
	return matriz_new

matriz_busca = procurar_arquivo()


if matriz_busca:
	print('Conteúdo da Matriz Lida Antes de Ordenar:')
	print('-'*41)
	print(matriz_busca)
	vals = 0
	valsr = 0
	ordenar_matriz = 0
	maior = 0

	for matriz_new in matriz_busca.split('\n'):
		matriz = matriz_new.strip().split()
		matriz = [int(i) for i in matriz]
		soma = sum(matriz)
		if soma > maior:
			maior = soma
			ordenar_matriz = matriz
			valsr = vals
		vals += 1
	vals = 0
	novo_conteudo = ''
	for matriz_new in matriz_busca.split('\n'):
		if vals == valsr:
			matriz_new = ordenar(ordenar_matriz)
		novo_conteudo += f'{str(matriz_new)}\n'
		open(nome_arquivo,'w+',encoding='utf-8').write(f'{str(novo_conteudo)}\n')
		vals += 1

	print('-'*52)
	print('Conteúdo da Matriz Após Ordenar Linha de Maior Soma:')
	print('-'*52)
	print(novo_conteudo)


