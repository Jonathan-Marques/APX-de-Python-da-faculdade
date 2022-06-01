import struct

valor = 0
def processarArquivo(nomeArquivo, resultadoSorteio):
    print("Conteúdo do Arquivo de Apostas", nomeArquivo + ":")

    totalApostas = 0
    acertos = dict()
    for qtdAcertos in range(3, 7):
        acertos[qtdAcertos] = set()

    with open(nomeArquivo, "r") as arquivo:
        for linha in arquivo:
            print(linha, end="")

            if (len(linha.split()) > 1):
                totalApostas = totalApostas + 1
                numerosJogados = set(map(int, linha.split()))
                qtdAcertos = len(resultadoSorteio & numerosJogados)
                if (qtdAcertos >= 3):
                    acertos[qtdAcertos].add(valor)

    return totalApostas, acertos


def imprimeResultados(totalAposta, acertos):
    if (totalAposta == 0):
        print("“Nenhuma Aposta!!!", acertos,'e', valor, )



def main():
    nomeArquivo = input() + ".txt"
    resultadoSorteio = set(map(int, input().split()))

    try:
        totalAposta, acertos = processarArquivo(nomeArquivo, resultadoSorteio)
        imprimeResultados(totalAposta, acertos)
    except IOError:
        print('O arquivo não foi encontrado')


main()