def calculadiferenca(xp, yc):
            d = ((xp[0] - yc[0]) ** 2) + ((xp[1] - yc[1]) ** 2)
            resultado = d**(float)(1)/(2)
            return resultado


def ciculodentro(circulo):
    if len(circulo) < 2:
        print("Mais Distantes: Não existem pelo menos dois pontos!!")
    else:
        xp = circulo[0]
        yc = circulo[1]
        maiorDistancia = calculadiferenca(xp, yc)

        for i in range(len(circulo)):
            for j in range(i + 1, len(circulo)):
                distAtual = calculadiferenca(circulo[i], circulo[j])
                if distAtual > maiorDistancia:
                    xp = circulo[i]
                    yc = circulo[j]
                    maiorDistancia = distAtual


        print(yc, " está dentro do círculo:",xp)
    return None


def ciculoEstadentro(circulo):
    if len(circulo) < 2:
        print("Mais Próximos: Não existem pelo menos dois pontos!!")
    else:
        xp = circulo[0]
        yc = circulo[1]
        menorDistancia = calculadiferenca(xp, yc, )


        for i in range(len(circulo)):
            for j in range(i + 1, len(circulo)):
                distAtual = calculadiferenca(circulo[i], circulo[j])
                if distAtual < menorDistancia:
                    xp = circulo[i]
                    yc = circulo[j]

                    menorDistancia = distAtual

        print( xp," está dentro do círculo", yc )
    return None


def mostraMedia(circulo):
    if len(circulo) == 0:
        print("Não existe média!!!")
    else:
        somaX = 0
        somaY = 0
        qtd = 0
        for (x, y, r) in circulo:
            somaX += x
            somaY += y
            qtd += 1
            prdut = somaY / somaX
            pc = somaY / qtd - qtd*2
        print("Quantidade de Pontos Dentro de Círculo:", round(prdut, 0))
        print("Percentual de Pontos Dentro:", round(pc, 0), "%")

        return None


# Programa Principal
paresLidos = []
par = input().split()
x = int(par[0])
y = int(par[1])
r = int(par[2])

par = input()
while par !="":
    x, y = par.split()
    paresLidos.append((int(x), int(y), int(r)))
    par = input()



ciculoEstadentro(paresLidos)
ciculodentro(paresLidos)
print("Quantidade de Ponto(s) Processado(s):", len(paresLidos))

mostraMedia(paresLidos)