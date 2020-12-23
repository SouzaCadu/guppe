"""
leia uma matriz 5 X 10 que se refere a respostas de 10 questões
de múltipla escolha, referente a 5 alunos.
leia também um vetor de 10 posições contendo o gabarito
das questões, que pode ser "a", "b" "c", "d"
compare as respostas com o gabarito e calcule o
resultado de cada aluno
"""

import random
from random import randint, choice
import string
from collections import Counter

letras = string.ascii_lowercase[:4]
respostas = []
cod_aluno = []

for i in range(5):
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

for i in range(5):
    notas_finais[i] = dict(Counter(notas[i]))
for j in range(len(notas_finais)):
    print(f'A nota do aluno {j} foi {notas_finais[j].get(1, 0)}.')
