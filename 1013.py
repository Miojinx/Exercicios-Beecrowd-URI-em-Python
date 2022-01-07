
numeros = input().split()
a, b, c = numeros
maiorab = (int(a) + int(b) + abs(int(a) - int(b))) / 2
maior = (maiorab + int(c) + abs(maiorab - int(c))) / 2
print("{0} eh o maior" .format("%d" % maior))

