"""
faça um programa para gerar um número aleatório entre 1 e 1000
o usuário deve tentar acertar qual o número gerado,
a cada tentativa o programa deverá informar se o
valor que o usuário informou é maior ou menor que o número gerado
o programa deve informar o número de tentativas até o acerto
"""

from random import randint

rand = randint(1, 1000)

print("Descubra o número aleatório entre 1 e 1000")

palpite = int(input("Informe o palpite: "))

contador = 1

while palpite != rand:
    if palpite < rand:
        print("O valor do palpite é menor que o número gerado.")
        contador += 1
        palpite = int(input("Informe o palpite: "))
    elif palpite > rand:
        print("O valor do palpite é maior que o número gerado.")
        contador += 1
        palpite = int(input("Informe o palpite: "))
if palpite == rand:
    print(f"Parabéns você acertou! Em {contador} tentativas.")
