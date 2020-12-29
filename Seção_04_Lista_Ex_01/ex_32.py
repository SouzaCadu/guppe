"""
Leia um número inteiro e imprima a soma do sucessor de seu triplo
com o antecessor de seu dobro
"""

print(f"Insira um número inteiro para \n"
      f"saber a soma do sucessor de seu triplo \n"
      f"com o antecessor de seu dobro.")

print(f"Insira um valor:")

n = int(input())

s_t = (n * 3) + 1
a_d = (n * 2) - 1

print(f"O resultado é {s_t + a_d}.")