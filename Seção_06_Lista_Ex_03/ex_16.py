"""
faça um programa que leia um número inteiro positivo ímpar N
e imprima todos os números ímpares de 1 até N em ordem decrescente
"""

n = 0

print("Digite um número inteiro ímpar para saber todos os,\n"
      "ímpares de 1 até N em ordem decrescente.")

while n % 2 == 0:
    n = int(input("Digite um número inteiro ímpar: "))
    if n % 2 != 0:
        for i in range(n, -1, -2):
            print(i, end=" ")
