"""
escreva um programa que leia um número inteiro e calcule a soma de todos os divisores
desse número, com exceção dele próprio
"""

print("Insira um número para saber a soma de todos os seus\n"
      "divisores, execeto ele mesmo.")

n = int(input("Digite um número inteiro: "))

soma = 0

for i in range (1, n):
    if n % i == 0:
        soma = soma + i
print(f"A soma dos divisores de {n} exceto ele é {soma}.")