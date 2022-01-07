contagemPar = 0
contagemImpar = 0
contagemPos = 0
contagemNeg = 0
for i in range(5):
    num = float(input())
    if num % 2 == 0:
        contagemPar += 1
    if num % 2 != 0:
        contagemImpar += 1
    if num > 0:
        contagemPos += 1
    if num < 0:
        contagemNeg += 1
print(f"{contagemPar} valor(es) par(es)")
print(f"{contagemImpar} valor(es) impar(es)")
print(f"{contagemPos} valor(es) positivo(s)")
print(f"{contagemNeg} valor(es) negativo(s)")