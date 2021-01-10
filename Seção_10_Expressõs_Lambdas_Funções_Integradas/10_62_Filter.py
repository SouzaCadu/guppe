"""
Filter

Serve para filtrar dados em uma determinada coleção.
Recebe uma função e um iterável.
Após ser processada ela não fica na memória.

Map: recebe dois parametros, uma função e um iterável, e retorna um objeto mapeando
     a função para elemento iterável
Filter: recebe dois parametros, uma função e um iterável, e retorna um objeto filtrando
     apenas os elementos de acordo com a condição da função

Exemplos:


import statistics

dados = [1.3, 2.7, 0.8, -4.1, 4.3, -0.1, -8.7, 9.4]

media = statistics.mean(dados)

print(f"Media {media:.2f}")

res = filter(lambda x: x > media, dados)

print(list(res))

paises = ["", "China", "Japão", "", "Argentina", "", "", "Brasil", "Quenia",
          "", "Ucrania", "Irã", "", "Canada", "Porto Rico"]

print(paises)

res = filter(None, paises)

print(list(res))

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
    {"usuário": "andrew_ng", "tweets": []},
    {"usuário": "ze_dirceu", "tweets": []},
    {"usuário": "flordelis_09123", "tweets": []},
    {"usuário": "dalai_lama1233", "tweets": []}
]

inativos = list(filter(lambda usuario: len(usuario["tweets"]) == 0, usuarios))

print(inativos)

inativos = list(filter(lambda usuario: not usuario["tweets"], usuarios))
# lista vazia transformada em boolean é sempre falso

print(inativos)

nomes = ["Vanessa", "Ana", "Maria", "Leticia", "Tereza", "Gabriela", "Mara", "Julia"]

lista = list(map(lambda nome: f"Sua instrutora é {nome}",
                 filter(lambda nome: len(nome) < 4, nomes)))

print(lista)

"""
