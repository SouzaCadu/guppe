"""
Faça uma prova de matemática para crianças que estão aprendendo
a somar números inteiros menores do que 100. Escolha números aleatórios
entre 1 e 100, e mostre na tela a pergunta: qual é a soma de a + b,
onde a e b são os números aleatórios. Peça a resposta. Faça cinco
perguntas ao aluno, e mostre para ele as perguntas e as respostas
corretas, além de quantas vezes o aluno acertou
"""

from random import randint

print("Prova de matemática")

n1, n2 = randint(0, 100), randint(0, 100)

print(f"1 - Qual a soma de {n1} + {n2}?")

r1 = int(input("Valor da soma é:"))

n3, n4 = randint(0, 100), randint(0, 100)

print(f"2 - Qual a soma de {n3} + {n4}?")

r2 = int(input("Valor da soma é:"))

n5, n6 = randint(0, 100), randint(0, 100)

print(f"3 - Qual a soma de {n5} + {n6}?")

r3 = int(input("Valor da soma é:"))

n7, n8 = randint(0, 100), randint(0, 100)

print(f"4 - Qual a soma de {n7} + {n8}?")

r4 = int(input("Valor da soma é:"))

n9, n10 = randint(0, 100), randint(0, 100)

print(f"5 - Qual a soma de {n9} + {n10}?")

r5 = int(input("Valor da soma é:"))

print("Respostas:")

print(f"1 - {n1} + {n2} = {n1 + n2}")
print(f"2 - {n3} + {n4} = {n3 + n4}")
print(f"3 - {n5} + {n6} = {n5 + n6}")
print(f"4 - {n7} + {n8} = {n7 + n8}")
print(f"5 - {n9} + {n10} = {n9 + n10}")

acertos = 0

if r1 == n1 + n2:
    acertos += 1
if r2 == n3 + n4:
    acertos += 1
if r3 == n5 + n6:
    acertos += 1
if r4 == n7 + n8:
    acertos += 1
if r5 == n9 + n10:
    acertos += 1

print(f"O total de acertos foi de {acertos}.")
