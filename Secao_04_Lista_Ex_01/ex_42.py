"""
Adicione 5% sobre um valor e subtraia 7% do mesmo valor
"""

g = 0.05
i = 0.07

print(f"Para saber o valor liquido a receber \n"
      f"insira o valor do salário base:")

sb = float(input())

print(f"O valor liquido a receber é {sb * (1 + g) - (sb * i)}.")