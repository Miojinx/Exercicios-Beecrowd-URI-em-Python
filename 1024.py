from math import ceil

n = int(input())
for i in range(n):
    texto = str(input())
    passada1 = ""
    for j in texto:
        if (j.isalpha() == True):
            passada1 += chr(ord(j) + 3)
        else:
            passada1 += j
    passada2 = passada1[::-1]
    metade = ceil(len(passada2) / 2)
    texto2 = passada2[-metade::]
    texto3 = ""
    for k in texto2:
        texto3 += chr(ord(k) - 1)
    final = passada2.replace(texto2, texto3)
    print(final)
