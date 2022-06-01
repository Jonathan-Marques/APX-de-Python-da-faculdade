c1 = ""
c2 = ""
print("O programa fará o complemento de 2 no valor inserido")
b = input("Digite um número binário: ")
for i in range(len(b)):
    if (b[i] == "0"):
        c1 = c1 + "1"
    elif (b[i] == "1"):
        c1 = c1 + "0"
if (c1[1] == "1"):
    c1[-1] =str(1)

tamanho = len(c1) - 1
for i in range(tamanho + 1):
    print(i)
    print(tamanho)
    c2 = c2 + c1[i]
print("inicio:", b)
print("c1:", c1)
print("c2:", c2)