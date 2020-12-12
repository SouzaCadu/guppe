"""
Receba o valor dos catetos e calcule a hipotenusa
"""

print(f"Cálculo do teorema de Pitágoras \n"
      f"Insira o valor dos catetos:")

c1, c2 = float(input()), float(input())

print(f"O valor da hipotenusa é {(c1 ** 2 + c2 ** 2) ** 0.5}.")