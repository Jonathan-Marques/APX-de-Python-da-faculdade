lista= 0
def somarbinario( a: str, b: str) -> str:
    global i
    res =""
    carry = 0
    a, b = a [::-1], b[::-1]
    for i in range(max(len(a), len(b))):
        digitA = ord(a[i]) - ord("0") if i < len(a) else 0
        digitB = ord(b[i]) - ord("0") if i < len(b) else 0

        total = digitA + digitB + carry
        char = str (total % 2)
        res = char + res
        carry = total // 2

    if carry:
        res = "1" + res
        return res

    else:
        var = lista[i]
        impLista(lista)
        if lista[0]== "0":
            lista.insert(0, "1")
            impLista (lista)
            impLista(lista)
        else:
            print('não esta codificado em binario', carry)


def impLista():
    print("", impLista)


    somarbinario(a,b)

a = input()
b = 1

print("", impLista)