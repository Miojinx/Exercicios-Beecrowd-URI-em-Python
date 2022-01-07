notas = input().split()
n1, n2, n3, n4, = notas
media = (float(n1) * 2 + float(n2) * 3 + float(n3) * 4 + float(n4) * 1) / 10
print("Media: %.1f" % media)
if media >= 7:
    print("Aluno aprovado")
if media < 5:
    print("Aluno reprovado")
if 5 <= media < 7:
    print("Aluno em exame")
    notaexame = float(input())
    print("Nota do exame: %.1f" % notaexame)
    novamedia = (media + notaexame) / 2
    if media >= 5:
        print("Aluno aprovado")
    if media < 5:
        print("Aluno reprovado")
    print("Media final: %.1f" % novamedia)