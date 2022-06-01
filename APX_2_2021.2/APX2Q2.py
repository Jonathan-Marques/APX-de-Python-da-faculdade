#Jonathan Santiago Marques, Polo: Itaguai, Mat: 20213050125
# # AP2X - Questão 2
import os.path
import struct
Natal = struct.Struct("20s 20s 100s")
printInfo = False
def decodifica_dados_Natal(bloco):
    campos = Natal.unpack(bloco)
    nome = campos[0].decode("utf-8")
    parentesco = campos[1].decode("utf-8").strip(chr(0))
    presente = campos[2].decode("utf-8").strip(chr(0)).strip('\n')
    return nome, parentesco, presente


arquivo = input().strip()
def dados_natal():
		if os.path.exists(arquivo):
			return open(arquivo,'r',encoding='utf-8').read().strip()

lista_presente = dados_natal()
if lista_presente:
	for nome in lista_presente.split('\n'):
		if not '#' in nome: continue
		nome = nome.split('#')
	parentesco = input().strip()

	if parentesco in lista_presente:
		for i in lista_presente.strip().split('\n'):
			if not '#' in i: continue
			lista = i.split('#')
			nome = lista[0]

			if parentesco == nome:
				parente = lista[1]
				presente = lista[2]
				presente_nome = ''
				total = 0

				for p in presente.split(';'):
					presente, valor = p.split('&')
					presente_nome += presente + '\n'
					total += float(valor.replace(',','.'))

				print('Para comprar os presentes para {}, que é meu/minha''\n'
				'{}, gastarei R$ {}.''\n'
				'Os itens da lista para {} são:''\n''{}'.format(nome,parente,total,nome, presente_nome))

	else:
		print('não está na lista!')
