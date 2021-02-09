"""
List Comprehension

- utilizando List Comprehension podemos gerar novas listas com dados processados
de outro iterável

# sintaxe:

[ dado for dado in iterável ]

Primeira parte: for dado in iterável

Segunda parte: dado, pode ser qualquer coisa


# Exemplos

numeros = range(6)

res = [numero * 10 for numero in numeros]

res1 = [numero / 2 for numero in numeros]


def quadrado(valor):
    return valor ** 2


res2 = [quadrado(numero) / 2 for numero in numeros]


print(res)
print(res1)
print(res2)

# List Comprehension vs Loop

numeros_dobrados = []

for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

print([numero * 2 for numero in numeros])

# Outros exemplos

nome = "Geek University"

print([letra.upper() for letra in nome])

amigos = ["maria", "julia", "pedro", "felipe", "ana", "larissa", "luisa", "tomas"]

print([amigo.title() for amigo in amigos])

print([i * 3 for i in range(1, 25)])

print([bool(valor) for valor in [0, [], "", True, 3.14]])

print([str(valor) for valor in range(1, 11)])

"""
