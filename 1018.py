n = int(input())
while n > 1000000:
    n = int(input())
print(n)
cedulas = [100, 50, 20, 10, 5, 2, 1]
for i in cedulas:
    qtdNotas = int(n/i)
    print(f"{qtdNotas} nota(s) de R$ {i},00")
    n = n - qtdNotas * i