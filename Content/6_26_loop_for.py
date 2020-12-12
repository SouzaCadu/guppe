"""
Loop for

Loop -> estrutura de repetição
for -> uma dessas estruturas

# for item (in iterável):
    //execute o loop

utilizamos loops para iterar sobre sequencias ou sobre valores
iteráveis, por exemplo, strings, listas, range

nome = "Geek University"
lista = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 13, 15]
numeros = range(1, 10)

# Exemplo 1 - Iterando sobre um string
for letra in nome:
    print(letra)
    print(letra, end="")  # sem pular linha

# Exemplo 2 - Iterando sobre uma lista
for numero in lista:
    print(numero)

# Exemplo 3 - Iterando sobre um range
for numero in numeros:
    print(numero)

# Exemplo 4 - Iterando sobre string acessando o indice
for indice, letra in enumerate(nome):
    print(indice, letra)  # i = indice, v = valor

for _, letra in enumerate(nome):
    print(letra)  # _ descarta o indice, v = valor

for valor in enumerate(nome):
    print(valor)   # imprime uma tupla letra e valor
    print(valor[0])  # imprime valor
    print(valor[1])  # imprime letra

# Exemplo recebendo dados do usuário
qtd = int(input("Quantas vezes esse loop deve ser processado?"))

for n in range(1, qtd + 1):
    print(n)

soma = 0
for n in range(1, qtd + 1):
    num = int(input(f"Informe o {n}/{qtd} valor:"))
    soma = soma + num
print(f"A soma é {soma}.")

# Comandos com strings

print(nome + nome)  # concatena string
print(nome * 3)  # repete a string

for num in range(1, 11):
    print(f"{nome * num}")

# Imprimindo emojis, fonte https://apps.timwhitlock.info/emoji/tables/unicode
# código do emoji = U+1F62D
# transformando emoji em unicode de U+1F62D para U0001F62D

emoji = '\U0001F62D'

for _ in range(3):
    for num in range(1, 11):
        print(f"{emoji * num}")

"""