import struct
Natal = struct.Struct("20s 20s 100s")

def main():
    try:
        with open("natal.txt", "r") as arquivoTxt:
            with open("natal.bin", "wb") as arquivoBin:
                for linha in arquivoTxt:
                    entrada = linha.split('#')
                    if (len(entrada) > 1):
                        Nome = entrada[0]
                        parentesco = entrada[1]
                        presente = entrada[2]
                        bloco = Natal.pack(Nome.encode("utf-8"), parentesco.encode("utf-8"), presente.encode("utf-8"))
                        arquivoBin.write(bloco)
        print("Arquivo binário criado.")
    except IOError:
        print('Arquivo txt não encontrado.')

main()