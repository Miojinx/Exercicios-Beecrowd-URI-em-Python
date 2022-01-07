dias = int(input())
ano = dias // 365
dias = dias % 365
mes = dias // 30
dias = dias % 30
print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dias))