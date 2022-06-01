#from collections import Counter
#resultado = []
#resultado_int = []
#apos_int = []
#apostas = []
#apostas_int = []
#comuns = []
#lista_verificacao = []
#lista_verificacao_1 =[]

#função para lê da entrada padrão os números apurados e armazenar em uma lista
#def sorteio(valor_resultado):
#   for i in range(1,7):
#       print("\nDigite o",i,"º número sorteado:")
#       numero = input()
#       valor_resultado.append(numero)


#lê o nome do arquivo de entrada
#nome = input("Digite o nome do arquivo: ")

#Mostra o conteúdo do arquivo na saída padrão
#arquivo = open(nome, 'r')
#print("Conteúdo do arquivo", nome,":")
#print(arquivo.read())
#arquivo.close()

#Função para lê da entrada padrão os números apurados e armazenar em uma lista
#sorteio(resultado)

#Manipula o arquivo txt
#arquivo = open(nome, 'r+')
#for linha in arquivo:
    #   linha = str(linha)
    #linhaa = linha.split()
    #apostas.append(linhaa)
#arquivo.close()

#Converte as listas para valores inteiros e retira os valores comuns através de um "SET"
#for i in range(len(apostas)):
    #   apos_int = list(map(int,apostas[i]))
    #resultado_int = list(map(int, resultado))
    #comuns.append(set(resultado_int) & set(apos_int))

#Converte os sets com os valores repetidos em uma lista e faz a contegem de elementos de cada sublista
#for i in range (len(comuns)):
    #   lista_verificacao.append(list(comuns[i]))
# lista_verificacao_1.append(len(lista_verificacao[i]))

#Saída formatada com os valores em um dicionário
#print("\nQuantidades de Apostas Premiadas:")
#for k,v in Counter(lista_verificacao_1).items():
#   print(f'Com {k} acerto(s) tivemos: {v} aposta(s)')




import os.path
NUMERO_DEZENAS  =  6
nome_arquivo = input() + ".txt"
aposta = input()
def procurar_arquivo():
		if os.path.exists(nome_arquivo):
			return open(nome_arquivo,'r',).read().strip()

sorteio = procurar_arquivo()


if sorteio:
	print('Conteúdo do Arquivo apostas01:')
	print('-'*41)
	print(sorteio)

def  existeNumero ( numeros , n ):
	return  n  in  numeros

print('')
print('Quantidades de Apostas Premiadas:')

def  contaAcertos ( sorteio , aposta ):
    acertos  = 0
    for  i  in range( 0 , NUMERO_DEZENAS ):
        nroAposta  =  aposta [ i ]
        if (existeNumero ( sorteio , nroAposta )):
            acertos +=  1
    return  acertos



nroAcertos  =  contaAcertos ( sorteio , aposta )
ocorrencias = sorteio.count(aposta)



print("    Com 6 acertos tivemos: {} aposta(s)".format(ocorrencias))
print("    Com 5 acertos tivemos: {} aposta(s)".format(nroAcertos - 5))
print("    Com 4 acertos tivemos: {} aposta(s)".format(nroAcertos - 3))
print("    Com 3 acertos tivemos: {} aposta(s)".format( nroAcertos - 6))
