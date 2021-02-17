"""
Se o número for positivo calcular o log, se negativo "Número inválido".
"""

from math import log

v1 = float(input("Digite um número positivo para saber o valor do logaritmo:"))

if v1 > 0:
    print(f"O valor do logaritmo é {log(v1):.2f}.")
else:
    print("Número inválido.")
