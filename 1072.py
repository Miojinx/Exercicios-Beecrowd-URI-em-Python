contagemIn = 0
contagemOut = 0
n = int(input())
while n != 0:
    n -= 1
    num = int(input())
    if 10 <= num <= 20:
        contagemIn += 1
    else:
        contagemOut += 1
print(f"{contagemIn} in")
print(f"{contagemOut} out")