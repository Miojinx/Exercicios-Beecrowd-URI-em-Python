contagem = 0
for i in range(5):
    num = float(input())
    if num % 2 == 0:
        contagem+=1
print(f"{contagem} valores pares")