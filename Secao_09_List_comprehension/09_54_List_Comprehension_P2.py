"""
List Comprehension

Podemos adicionar estruturas condicionais lógicas


"""

# Exemplos

numeros = range(1, 30)

pares = [i for i in numeros if i % 2 == 0]

print(pares)

impares = [i for i in numeros if i % 2 != 0]

print(impares)

# Refatorando

pares = [i for i in numeros if not i % 2]

print(pares)

impares = [i for i in numeros if i % 2]

print(impares)

resultado = [i * 2 if i % 2 == 0 else i / 2 for i in numeros]
print(resultado)