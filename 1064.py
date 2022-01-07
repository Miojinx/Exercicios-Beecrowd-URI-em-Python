soma = 0
positivos = 0
for i in range(6):
    numero = float(input())
    if numero > 0:
        soma += numero
        positivos += 1
media = soma/positivos
print("{0} valores positivos\n{1}".format(positivos, "%.1f" % media))