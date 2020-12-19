"""
Módulo Collections - Named Tuple

São tuplas para as quais especificamos um nome, para a tupla e para os parametros
facilitando o acesso a informação.

Aceita os mesmo métodos usados em tuplas
"""

from collections import namedtuple

cachorro1 = namedtuple("cachorro", "raça idade origem")
cachorro2 = namedtuple("cachorro", "raça, idade, origem")
cachorro3 = namedtuple("cachorro", ["raça", "idade", "origem"])

ray = cachorro3(raça="Akita", idade=2, origem="Japão")
print(ray)
print(ray[0])
print(ray[1])
print(ray[2])

# ou

print(ray.raça)
print(ray.idade)
print(ray.origem)

# ou

print(ray.index("Japão"))