"""
Dadas 3 notas calcule a média ponderada e a situação do aluno
- n1 peso 2, n2 peso 3, n3 peso 5
- se média entre:
    (0 - 2,9) reprovado
    (3 - 4,9) recuperação
    (5 - 10,0) aprovado
"""

from sys import exit

print("Informe as três notas para saber a média \n"
      "e a situação do aluno:")
print()

n1 = float(input("Trabalho de laboratório:")) * 0.2

if n1 < 0:
    exit(print("Valor inválido. Programa finalizado."))

n2 = float(input("Avaliação semestral:")) * 0.3

if n2 < 0:
    exit(print("Valor inválido. Programa finalizado."))

n3 = float(input("Exame final:")) * 0.5

if n3 < 0:
    exit(print("Valor inválido. Programa finalizado."))

mf = n1 + n2 + n3

if 0 <= mf <= 2.9:
    print(f"{mf:.2f}, aluno reprovado.")
elif 3 <= mf <= 4.9:
    print(f"{mf:.2f}, aluno em recuperação.")
else:
    print(f"{mf:.2f}, aluno aprovado.")
