"""
Sorted

Não é igual ao atributo sort() que só funciona em listas.
Sorted funciona com qualquer iterável. Não altera o elemento original,
retorna um novo objeto

Exemplos

"""

numeros = [9, 8, 7, 3, 4, 1, 0, 11, 10, 12, 5, 6, 2]

print(numeros)

print(sorted(numeros))

print(tuple(sorted(numeros)))

print(set(sorted(numeros)))

print(numeros)

print(sorted(numeros, reverse=True))


usuarios = [
    {"usuário": "lucas", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"usuário": "carla", "tweets": ["Eu adoro meu cachorro", "Eu amo filmes de terror"]},
    {"usuário": "teixeira", "tweets": []},
    {"usuário": "jj_watt", "tweets": ["Go Texans!!!"]},
    {"usuário": "trump_01", "tweets": ["Make America Great Again"]},
    {"usuário": "turco_loco", "tweets": ["por mais esporte nas ruas", "Por mais pistas de skate"]},
    {"usuário": "osama", "tweets": ["Make my way at home learning to fly", "Holiday in Camboja!!!", "Going to California!!"]},
    {"usuário": "puttin_78912", "tweets": ["Vodka rules"]},
    {"usuário": "xin_jin_ping", "tweets": ["I gonna take my horse to the Old Town Road", "Doom 2"]},
    {"usuário": "andrew_ng", "tweets": [], "tema": []},
    {"usuário": "ze_dirceu", "tweets": [], "tema": []},
    {"usuário": "flordelis_09123", "tweets": [], "tema": []},
    {"usuário": "dalai_lama1233", "tweets": [], "tema": []}
]

print(sorted(usuarios, key=len, reverse=True))

print(sorted(usuarios, key=lambda usuario: usuario["usuário"]))

print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

musicas = [
    {"título": "Creeping Death", "repetições": 12},
    {"título": "American Jesus", "repetições": 15},
    {"título": "Before I Forget", "repetições": 20},
    {"título": "Aces High", "repetições": 45},
    {"título": "N. I. B.", "repetições": 32},
    {"título": "Black Sabbath", "repetições": 28},
    {"título": "Jailbreak", "repetições": 37}
]

print(sorted(musicas, key=lambda musica: musica["repetições"]))

print(sorted(musicas, key=lambda musica: musica["repetições"], reverse=True))
