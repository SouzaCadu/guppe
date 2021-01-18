""""
Trabalhando com módulos builtin

Módulos integrados que já vem instalados no Python e precisam ser importados para serem acessados.

Podemos usar um alias para o módulo

import random as rdm

print(rdm.random())

from random import random as rdm, randint as rdmint

print(rdm())
print(rdmint(1, 10))

Podemos importar todas as funções de um módulo

from random import *

print(random())

O importe de várias funções do mesmo pacote costuma ser feito com o uso do tuple

from random import (
    random,
    uniform,
    choice,
    shuffle,
    randint
)

for i in range(10):
    print(random())

for i in range(10):
    print(uniform(3, 7))

for i in range(6):
    print(randint(1, 61), end=", ")

jogadas = ["papel", "pedra", "tesoura"]
print(choice(jogadas))

cartas = ["k", "Q", "J", "A", "2", "3", "4", "5", "6", "7" ]

print(cartas)

"""
