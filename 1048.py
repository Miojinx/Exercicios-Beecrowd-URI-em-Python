def reajustes(sal):
    if 0 <= sal <= 400:
        reajGanho = (0.15 * sal)
        novoSal = sal + reajGanho
        porcentagem = 15
    elif 400.01 <= sal <= 800:
        reajGanho = (0.12 * sal)
        novoSal = sal + reajGanho
        porcentagem = 12
    elif 800.01 <= sal <= 1200:
        reajGanho = (0.10 * sal)
        novoSal = sal + reajGanho
        porcentagem = 10
    elif 1200.01 <= sal <= 2000:
        reajGanho = (0.07 * sal)
        novoSal = sal + reajGanho
        porcentagem = 7400
    elif sal > 2000:
        reajGanho = (0.04 * sal)
        novoSal = sal + reajGanho
        porcentagem = 4
    return novoSal, reajGanho, porcentagem


salario = float(input())
novoSalario, reajusteGanho, porcent = reajustes(salario)
print("Novo salário: %.2f" % novoSalario)
print("Reajuste ganho: %.2f" % reajusteGanho)
print(f"Em percentual: {porcent} %")