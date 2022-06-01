valori = 1  # inicia while

while valori !='':  # Quando o usuario digitar um valor vazio encerra o programa

    nota100, nota50, nota20, nota10, nota5, nota2, moeda1 = 0, 0, 0, 0, 0, 0, 0  # Zera Contador Notas (cedulas)
    try:
        valori = int(input())  # guarda o valor inicial
    except:
        break
    valor = valori  # Transfere o valor para outra variavel onde sera realizada a somatoria das cedulas

    # Notas (Cédulas)
    while valor >= 100:  # Somatoria de cedulas para cada variavel correspondente
        valor -= 100
        nota100 += 1
    while valor >= 50:
        valor -= 50
        nota50 += 1
    while valor >= 20:
        valor -= 20
        nota20 += 1
    while valor >= 10:
        valor -= 10
        nota10 += 1
    while valor >= 5:
        valor -= 5
        nota5 += 1
    while valor >= 2:
          valor -= 2
          nota2 += 1
    while valor >= 1:
        valor -= 1
        moeda1 += 1



    if valori != '':  # para não mostrar este print caso o usuario digite um valor em branco


        print(f"Trocando {valori:.0f} em:")

        if nota100 >= 1:
            print('     {} nota de 100 reais'.format(nota100))

        if nota50 >=1:
            print('     {} nota de 50 reais'.format(nota50))

        if nota20 >=1:
            print('     {} nota de 20 reais'.format(nota20))

        if nota10 >=1:
            print('     {} nota de 10 reais'.format(nota10))

        if nota5 >=1:
            print('     {} nota de 5 reais'.format(nota5))

        if nota2 >=1:
            print('     {} nota de 2 reais'.format(nota2))

        if moeda1 >=1:
            print('     {} moeda de 1 real'.format(moeda1))




# fim do while
