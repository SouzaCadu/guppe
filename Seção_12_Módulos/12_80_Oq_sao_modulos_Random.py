"""
Módulos e módulo Random

Em Python módulos são outros arquivos Python com funções. Devem ser instalados e/ou importados.

O módulo Random possui diversas funções para gerar números pseudo aleatórios.

Existem duas formas de utilizar um módulo:

Importando todo o módulo todas as funções, atributos, classes e propriedades que estiverem
dentro do módulo ficaram disponíveis em memória. O ideal é importar apenas as funções necessárias do módulo.

Por exemplo: import random

print(random.random())

Está indicado o módulo (random) e depois do ponto a função do módulo(random()).

Importando uma função específica de um módulo. Forma recomendada. O acesso a função é direto.

from random import random, uniform, randint, choice, shuffle

random: gera números reais pseudo aleatórios entre 0 e 1.
uniform: gera números reais pseudo aleatórios entre um intervalo estabelecido
randint: gera números inteiros pseudo aleatórios entre um intervalo estabelecido
choice: mostra um valor aleatório em um iterável
shuffle: embaralha dados em um iterável

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

shuffle(cartas)

print(cartas)

"""


