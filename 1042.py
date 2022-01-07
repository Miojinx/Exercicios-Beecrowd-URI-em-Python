numeros = list(map(int, input().split()))
numerosCrescente = sorted(numeros)
for i in range(3):
    print(numerosCrescente[i])
print()
for j in range(3):
    print(numeros[j])