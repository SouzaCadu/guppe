"""
faça um programa que simula o lançamento de dois dados n
vezes e tenha como saída:
- o número de cada dado
- a relação entre eles (>, <, =) de cada lançamento
"""

from random import randint

n = int(input("Digite 1 para girar os dados ou 2 para sair: "))

while n != 2:
    d1 = randint(1, 6)
    d2 = randint(1, 6)

    if d1 > d2:
        print(f"O resultado é {d1} > {d2}.")
        n= int(input("Digite 1 para girar os dados ou 2 para sair: "))
    elif d1 < d2:
        print(f"O resultado é {d1} < {d2}.")
        n = int(input("Digite 1 para girar os dados ou 2 para sair: "))
    elif d1 == d2:
        print(f"O resultado é {d1} = {d2}.")
        n = int(input("Digite 1 para girar os dados ou 2 para sair: "))
