"""
Faça um programa que leia 10 inteiros positivos,
ignorando não positivos, e imprima a média
"""

i = 1
soma = 0
print("Digite 10 números inteiros positivos \n"
      "para saber a média aritmética.")
while i <= 10:
    n = int(input("Digite um valor: "))
    if n > 0:
        soma = soma + n
        i = i + 1
    else:
        print("Número inválido")
print(f"A média aritmética dos números digitados é {soma/10:.2f}.")
