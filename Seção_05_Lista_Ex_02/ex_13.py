"""
calcule a média ponderada de 3 notas:
- n1 e n2 tem peso 1
- n3 tem peso 2
- a média para aprovação é maior ou igual a 60 pts
"""

print("Informe as 3 notas do aluno para saber a média.")
print()
n1 = float(input("Informe a nota da P1:")) * 10
n2 = float(input("Informe a nota da P2:")) * 10
n3 = float(input("Informe a nota da P3:")) * 10

mf = (n1 + n2 + n3 * 2) / 4

if mf >= 60:
    print(f"{mf}, aluno aprovado.")
else:
    print(f"{mf}, aluno reprovado.")
