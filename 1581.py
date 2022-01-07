n = int(input())
while n > 0:
    n -= 1
    linguas = []
    k = int(input())
    while k > 0:
        k -= 1
        linguas.append(input())
    s=linguas[0]
    for m in linguas:
        if m != s:
            s = "ingles"
    print(s)
