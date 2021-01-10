"""
Generators

Tuple comprehension, não retorna uma tupla, retorna um generator object iterável.
A partir do primeiro uso ele é apagado da memória.

Quando um list/dict/set comprehension puderem ser escritos como um generator, o generator é preferível, pois
ocupa menos memória. Logo o generator é mais performático.


Exemplos

nomes = ["carlos", "carla", "camilla", "carina", "vanessa", "julius"]

print(all(nome[0] == "c" for nome in nomes))

res = (nome[0] == "c" for nome in nomes)

print(type(res))

from sys import getsizeof

print(getsizeof("Geek"), getsizeof("Metallica"), getsizeof(120099083129083129381), getsizeof(True))

# tamanho dos objetos iteráveis

list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
dict_comp = getsizeof({x: x * 10 for x in range(1000)})
gen = getsizeof(x * 10 for x in range(1000))

print(f"Para fazer a mesma tarefa ocupamos em memoria\n"
      f"List comprehension: {list_comp} bytes \n"
      f"Set comprehension: {set_comp} bytes \n"
      f"Dict comprehension: {dict_comp} bytes \n"
      f"Generator expression: {gen} bytes")

gen = (x * 10 for x in range(1000))

for i in gen:
    print(i)

"""
