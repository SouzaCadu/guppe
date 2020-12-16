"""
Um funcionário recebe aumento anual. Em 1995 contratado por 2000
Em 1996 recebeu um aumento 1.5%. A partir de 1997, os aumentos sempre
correspondem ao dobro do ano anterior.
Calcule o salário atual do funcionário.
"""


salario = 2000
taxa = 0.015
ano = 1995
ano_atual = 2020

while ano < ano_atual:
    ano += 1
    salario = (salario * taxa) + salario
    print(f'Ano = {ano}, Salário = R$ {salario:.2f}, Taxa = {100 * taxa}%')  # Para 'DEBUG'
    taxa = taxa * 2

print(f'Em {ano} o salário será de R$ {salario:.2f}.')