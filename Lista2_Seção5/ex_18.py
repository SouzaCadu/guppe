"""
Exibir quatro operações matemáticas, o usuário escolhe uma, executa e sai
"""

from sys import exit

operacao = input("Escolha a operação ['*']['/']['+']['-']")

n1 = float(input("Digite o primeiro valor:"))
n2 = float(input("Digite o segundo valor:"))

print()
if operacao == "*":
    print(f"O resultado do cálculo é{n1 * n2:.2f}.")
elif operacao == "/":
    print(f"O resultado do cálculo é{n1 / n2:.2f}.")
elif operacao == "+":
    print(f"O resultado do cálculo é{n1 + n2:.2f}.")
elif operacao == "-":
    print(f"O resultado do cálculo é{n1 - n2:.2f}.")
else:
    print("Operacao inválida.")
    exit()
