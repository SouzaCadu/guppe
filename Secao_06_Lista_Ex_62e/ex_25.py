"""
Faça um programa que some todos os números naturais abaixo de 1000
que são múltiplos de 3 ou 5
"""

soma = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        soma = soma + i
print(f"A soma de todos os números naturais menores que 1000\n"
      f"que são divisiveis por 3 ou 5 é {soma}")