"""
Cálculo de média geométrica, ponderada, harmônica e aritmética
"""

from sys import exit

print("Escolha o tipo de média: \n"
      "1 - Geométrica \n"
      "2 - Ponderada \n"
      "3 - Harmônica \n"
      "4 - Aritmética")

media = int(input("Digite o valor escolhido:"))

if media not in (1, 2, 3, 4):
    exit(print('Opção inválida!'))

n1 = float(input("Digite o primeiro valor:"))
n2 = float(input("Digite o segundo valor:"))
n3 = float(input("Digite o terceiro valor:"))

if media == 1:
    print(f"Média geométrica {((n1 * n2 * n3) ** 1/3):.2f}")
elif media == 2:
    print(f"Média ponderada {((n1 + 2 * n2 + 3 * n3) / 6):.2f}")
elif media == 3:
    print(f"Média harmônica {(1 / (1 / n1 + 1 / n2 + 1 / n3)):.2f}")
elif media == 4:
    print(f"Média aritmética {(n1 + n2 + n3) / 3 :.2f}")
