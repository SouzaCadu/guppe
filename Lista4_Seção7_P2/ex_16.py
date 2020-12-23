"""
faça um programa para corrigir uma prova com 10 questões de
multipla escolha (a, b, c, d) em uma turma com 3 alunos.
cada questão vale um ponto.
para cada aluno escreva a matricula, suas respostas, sua nota,
considere o criterio para aprovacao maior ou igual a 7.0
"""

import random
from random import randint, choice
import string
from collections import Counter

letras = string.ascii_lowercase[:4]
respostas = []
cod_aluno = []

for i in range(3):
    matricula = randint(100, 199)
    cod_aluno.append(matricula)

print(cod_aluno)

for i in range(3):
    aux = []
    for j in range(10):
        resposta = random.choice(letras)
        aux.append(resposta)
    respostas.append(aux)

print(respostas)

gabarito = []

for i in range(10):
    gabarito.append(random.choice(letras))

print(gabarito)

notas = []

for i in range(len(respostas)):
    aux = []
    for j in range(10):
        if respostas[i][j] == gabarito[j]:
            aux.append(1)
        else:
            aux.append(0)
    notas.append(aux)

print(notas)

notas_finais = dict()
status = ""

for i in range(3):
    notas_finais[i] = dict(Counter(notas[i]))

alunos_notas_finais = {cod_aluno[i]: notas_finais[i].get(1, 0) for i in range(0, len(cod_aluno))}

print(alunos_notas_finais)

for j in range(len(notas_finais)):
    if notas_finais[j].get(1, 0) >= 7:
        status = "aprovado"
    else:
        status = "reprovado"
    print(f'A nota do aluno {cod_aluno[j]} foi {notas_finais[j].get(1, 0)}, o aluno está {status}.')
