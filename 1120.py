d, n = input().split()
while d != "0" and n != "0":
    textoNovo = n.replace(d, "")
    if textoNovo == "":
        textoNovo = 0
    print(int(textoNovo))
    d, n= input().split()