qtdanos = int(input())
anterior = float(input())
atual = float(input())

antesAnterior = 0
print("No ano 1 há", anterior, "flores e no ano 2,", atual)

for i in range(2, qtdanos):
    antesAnterior = anterior
    anterior = atual
    atual = (anterior * 2) - (antesAnterior / 2)

print("Assim, no ano", qtdanos, "ha", round(atual, 2), "flores.")


