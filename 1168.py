num = int(input())
for p in range(1, num + 1):
    qtdled = 0
    x = input()
    for i in range(0, len(x)):
        if x[i] == '1':
            qtdled = qtdled + 2
        if x[i] == '2':
            qtdled = qtdled + 5
        if x[i] == '3':
            qtdled = qtdled + 5
        if x[i] == '4':
            qtdled = qtdled + 4
        if x[i] == '5':
            qtdled = qtdled + 5
        if x[i] == '6':
            qtdled = qtdled + 6
        if x[i] == '7':
            qtdled = qtdled + 3
        if x[i] == '8':
            qtdled = qtdled + 7
        if x[i] == '9':
            qtdled = qtdled + 6
        if x[i] == '0':
            qtdled = qtdled + 6
    print("{0} leds".format(qtdled))
