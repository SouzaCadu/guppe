"""
Se o número digitado for positivo calcule a raiz quadrada, se não retorne inválido
"""

import math

v1 = float(input("Insira um valor positivo para saber a raiz quadrada:"))

if v1 > 0:
    print(f"A raiz quadrada de {v1} é {math.sqrt(v1):.2f}")
elif v1 < 0:
    print(f"Número inválido.")
else:
    print(f"{v1} é igual a 0.")
