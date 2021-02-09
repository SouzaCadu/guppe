"""
Dictionary Comprehension

Sintaxe

{chave: valor for valor in iterável}

# Exemplos

numeros = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

quadrados = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrados)

numeros1 = range(5)

quadrados = {valor: valor ** 2 for valor in numeros1}

chaves = "abcde"

dicionario = {chaves[i]: numeros1[i] for i in range(0, len(chaves))}

print(dicionario)

res = {numero: ("par" if numero % 2 == 0 else "impar") for numero in numeros1}
print(res)

"""
