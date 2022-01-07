n = int(input())
for i in range(n):
    texto = input()
    n= int(input())
    textoNovo = ""
    for i in texto:
        posicao = ord(i) - n

        if (posicao < 65):
            textoNovo += chr(91 - (65 - posicao))
        else:
            textoNovo += chr(ord(i) - n)
    print(textoNovo)