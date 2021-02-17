"""
Escreva um programa que receba como entrada o valor do saque realizado pelo cliente
de um banco e retorne quantas notas de cada valor serão necessárias para atender ao
saque com a menor quantidade de notas possível.
Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1
"""

print("Dado o valor de saque desejado será calculada\n"
      "a menor quantidade de notas necessárias para\n"
      "atender o saque.")

valor_saque = int(input('Insira o valor que deseja sacar: '))
notas = [1, 2, 5, 10, 20, 50, 100]
notas_saque = []

notas.sort(reverse=True)

print(notas)

for i in range(len(notas)):
    while valor_saque - notas[i] >= 0:
        valor_saque -= notas[i]
        notas_saque.append(notas[i])

print(notas_saque)