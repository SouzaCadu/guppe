"""
Utilizando Lambdas

São funções anônimas. Podendo não ter entradas ou ter múltiplas entradas.

Sintaxe:

lambda parametro(s): retorno



# Exemplos

calc = lambda x: 3 * x + 1

print(calc(10))

print(calc(4))

nome_completo = lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()

print(nome_completo("   charles   ", "    xavier   "))

print(nome_completo("   ALICIA   ", "    KEYS   "))

amar = lambda: "Como não amar Python?"

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 * y + 3 ** z ** 0.5)

print(amar())

print(uma(10))

print(duas(23, 3))

print(tres(-3, 4, 7))

autores = ["Machado de Assis", "H. G. Wells", "Lima Barreto", "Fernando Pessoa", "Augusto dos Anjos",
           "Chico Xavier", "Orson Wells", "Ariano Suassuna", "Humberto Eco", "Nassin Nicholas Taleb"]

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(" ")[-1].lower())

print(autores)

def funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


print(funcao_quadratica(2, 3, -5)(2))
print(funcao_quadratica(-72, 34, 51)(2))


"""
