n = int(input())
for i in range(n):
    texto = input()
    metade = int(len(texto) / 2)-1
    resultado = texto[metade::-1] + texto[len(texto) - 1:metade:-1]
    print(resultado)