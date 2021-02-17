"""
faça um programa que leia um número N inteiro positivo ímpar e
imprima todos os números ímpares de 1 até N
"""

print("Informe a quantidade de números ímpares desejados,\n"
      "a partir de um número ímpar.")

n = 0
while n % 2 == 0:
    n = int(input("Digite um número ímpar: "))
    if n % 2 != 0:
        for i in range(1, n+1, 2):
            print(i, end=" ")
