linha1 = input().split()
linha2 = input().split()
calculo = (int(linha1[1])*float(linha1[2])) + (int(linha2[1])*float(linha2[2]))
print("VALOR A PAGAR: R$ %.2f"%calculo)