numero_par =[]
res =[]
quadrado = []
n = int(input())
j = int(input())
k = int(input())
cont = 3
res.append(j)
res.append(k)
if j % 2 == 0:
    numero_par.append(j)
if k % 2==0:
    numero_par.append(k)
while cont <= n:
    r = j + k
    res.append(r)
    if r % 2==0:
        numero_par.append(r)
    if r % 4==0:
        quadrado.append(r)
    j = k
    k = r
    cont +=1

print('os {} elementos da sequencia são:'.format(n), '{}'.format(res), end='.' '\n')

if n > 2:
    print("Os elementos pares da sequência são: {}".format(numero_par), end='.')
else:
    print('Não há elementos pares na sequência até a posição {}'.format(n))
if n > 10:
    print('\n''Dentre esses, os que são quadrado perfeito são [{}, {}]'.format(quadrado[0], quadrado[1]), end='.')
elif n > 2:
    print('Não há elemento par quadrado perfeito.')

