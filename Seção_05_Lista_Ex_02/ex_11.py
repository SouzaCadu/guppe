"""
Leia um número inteiro maior que zero e some seus algarismos
"""

import sys

v1 = int(input("Insira um número inteiro para saber a soma de seus algarismos:"))

if v1 < 0:
    sys.exit(print("Número inválido. Programa finalizado."))
else:
    v1 = str(v1)
    soma = 0
    for i in range(len(v1)):
        soma += int(v1[i])
    print(f"A soma dos algarismos é {soma}")
