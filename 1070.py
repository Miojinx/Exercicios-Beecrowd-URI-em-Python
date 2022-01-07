x = int(input())
numeros = []
for i in range(x, x+12):
    if i%2 != 0:
        numeros.append(i)
for j in range(6):
    print(numeros[j])