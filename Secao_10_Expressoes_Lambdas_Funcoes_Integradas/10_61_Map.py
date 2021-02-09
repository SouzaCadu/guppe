"""
Map

Mapeamento de função e valores. Utilizada uma vez ela zera, limpando a memória.
Tendo dados iteráveis + uma função ele irá mapear cada elemento dos dados e aplicar
a função a cada um.

Exemplos

from math import pi


def area_circulo(raio):
    return pi * raio ** 2


print(area_circulo(2))
print(area_circulo(7.8))

raios = [2, 3, 4, 5, 7.8, 10, 44]

areas = []
for raio in raios:
    areas.append(area_circulo(raio))
print(areas)

map_areas = map(area_circulo, raios)
print(list(map_areas))

print(list(map(lambda raio: pi * (raio ** 2), raios)))

cidades = [("Changai", 17), ("Moscou", 10), ("Kiev", 15), ("Istambul", 14), ("Dubai", 16.5), ("Dubrovnik", 13.5),
           ("Montevidéu", 20), ("São Paulo", 23.5), ("Santiago", 18.5), ("Bogotá", 19.5), ("Nairóbi", 20.5), ("Porto Príncipe", 25.5)]
print(cidades)

c_para_f = lambda dado: (dado[0], round((9 / 5) * dado[1] + 32))

print(list(map(c_para_f, cidades)))

"""
