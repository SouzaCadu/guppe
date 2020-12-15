"""
Escreva um programa que verifique quais os números
entre 1000 e 9999 (inclusive) possuem a
seguinte propriedade:
- a soma dos dois dígitos de mais baixa ordem
  com os dois de mais alta ordem elevada ao quadrado
  é igual ao próprio número
"""

for i in range(1000, 100000):
    j = str(i)
    soma = int(j[:2]) + int(j[2:])
    quad = soma ** 2
    if quad == int(i):
        print(i, end=" ")
