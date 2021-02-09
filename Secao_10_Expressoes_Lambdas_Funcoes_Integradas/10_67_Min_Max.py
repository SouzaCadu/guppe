"""
Min e Max

max() - retorna o maior valor de um iterável ou o maior de 2 ou mais elementos

min() - Retorna o menor valor de um iterável ou o menor de 2 ou mais elementos

# Exemplos:

lista = [1, 12, 14, 129, 98, 56, 3, 5, 7, 9]
tupla = (1, 12, 14, 129, 928, 56, 3, 5, 7, 9)
conjunto = {1, 1342, 14, 129, 98, 56, 3, 5, 7, 9}
dicionario = {"a": 1, "b": 12, "c": 14, "d": 129, "e": 98, "f": 56, "g": 3, "h": 349405, "i": 7, "j": 9}

print(max(lista))
print(max(tupla))
print(max(conjunto))
print(max(dicionario.values()))

print(max("Geek University"))

print(max(1, 34.98, 12.43, 50.98))

print(min(lista))
print(min(tupla))
print(min(conjunto))
print(min(dicionario.values()))

print(min("Geek University"))

print(min(1, 34.98, 12.43, 50.98))

nomes = ["Arya", "Voldemort", "Thomas", "York", "Duncan"]

print(max(nomes), min(nomes))

print(max(nomes, key=lambda nome: len(nome)), min(nomes, key=lambda nome: len(nome)))

musicas = [
    {"título": "Creeping Death", "repetições": 12},
    {"título": "American Jesus", "repetições": 15},
    {"título": "Before I Forget", "repetições": 20},
    {"título": "Aces High", "repetições": 45},
    {"título": "N. I. B.", "repetições": 32},
    {"título": "Black Sabbath", "repetições": 28},
    {"título": "Jailbreak", "repetições": 37}
]

print(max(musicas, key=lambda musica: musica["repetições"]), min(musicas, key=lambda musica: musica["repetições"]))

print(max(musicas, key=lambda musica: musica["repetições"])["título"])

print(min(musicas, key=lambda musica: musica["repetições"])["título"])


"""

