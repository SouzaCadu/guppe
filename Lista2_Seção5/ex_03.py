"""
Se o número inserido for positivo imprima a raiz quadrada,
se não imprima o número ao quadrado
"""

import math

v1 = float(input("Insira um número positivo para saber a raiz quadrada \n"
                 "ou negativo para saber o quadrado:"))

if v1 > 0:
    print(f"A raiz quadrada de {v1} é {math.sqrt(v1):.2f}.")
else:
    print(f"{v1} ao quadrado é {v1 ** 2}.")
