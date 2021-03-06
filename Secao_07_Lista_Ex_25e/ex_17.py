"""
leia uma matriz 10 x 3 com as notas de 10 alunos em 3 provas
escreva o número de alunos cuja pior nota foi na prova 1,
o número de alunos cuja pior nota foi na prova 2 e
o número de alunos cuja pior nota foi na prova 3
o critério de desempate é arbitrário, o aluno deve ser
contado apenas uma vez
"""

from random import randint
from collections import Counter

matriz1 = []
lista = []
valor = 0
pior_nota = Counter([])

for i in range(10):
    for j in range(3):
        lista.append(randint(0, 10))
    matriz1.append(list(lista))
    lista.clear()

for i in range(len(matriz1)):
    print(matriz1[i])
    print(matriz1[i].index(min(matriz1[i])))
    lista.append(matriz1[i].index(min(matriz1[i])))
pior_nota = Counter(lista)
print(pior_nota)
print(f'{pior_nota[0]} alunos tiveram a pior nota na prova 1.')
print(f'{pior_nota[1]} alunos tiveram a pior nota na prova 2.')
print(f'{pior_nota[2]} alunos tiveram a pior nota na prova 3.')
