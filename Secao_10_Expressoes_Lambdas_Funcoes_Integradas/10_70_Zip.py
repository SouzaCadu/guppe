"""
Zip

Cria um iterável que agrega os elementos de 2 ou mais iteráveis passados como entrada
o item criado será limitado pelo tamanho da menor entrada

lista1 = range(10)

lista2 = range(10, 20)

zip1 = zip(lista1, lista2)

print(zip1, type(zip1))

print(list(zip1))

zip1 = zip(lista1, lista2)
print(tuple(zip1))

zip1 = zip(lista1, lista2)
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

lista3 = range(20, 36)

zip2 = zip(lista1, lista2, lista3)

print(list(zip2))

tupla = 1, 2, 3, 4, 5, 6, 7

lista = range(7, 15)

dicionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

print(list(zip(tupla, lista, dicionario.values())))

dados = [(1, 2), (3, 4), (5, 6), (7, 8)]

print(list(zip(*dados)))


"""


prova1 = [90, 85, 78, 88]

prova2 = [89, 88, 84, 90]

alunos = ["Alex", "Maria", "Ana", "Charles"]

final1 = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

final2 = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(final1, dict(final2))
