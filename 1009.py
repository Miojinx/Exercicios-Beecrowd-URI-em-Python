nome = input()
salarioFixo = float(input())
totalVendas = float(input())
comissao = float(totalVendas * 0.15 )
total = salarioFixo + comissao
print("TOTAL = R$ %.2f" %total)