"""
faça um programa que leia um número indeterminado de idades de
indivíduos (pare quando for informada a idade 0),
e a calcule a média desse grupo
"""

print("Informe quantos valores desejados para descobrir a média,\n"
      "se valor igual a 0 encerra.")

n = int(input("Digite o valor desejado, zero para encerrar: "))

soma = 0
contador = 1

while n > 0:
    soma += n
    contador += 1
    n = int(input("Digite o valor desejado, zero para encerrar: "))
    if n <= 0:
        print(f"A a média dos valores informados é {soma / contador:.2f}")
        break
