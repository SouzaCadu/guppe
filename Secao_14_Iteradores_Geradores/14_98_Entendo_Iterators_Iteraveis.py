"""
O que é um Iterator (iterador) e Iterables

Iterator: é um objeto que pode ser iterado. Um objeto que retorna um dado, sendo um elemento por vez quando
uma função next() é chamada.

Iterables: Um objeto que irá retornar um iterator quando a função iter() for chamada.

#  Iterable
nome = "Geek"
[print(i) for i in nome]

iter1 = iter(nome)

print(next(iter1))  # G
print(next(iter1))  # e
print(next(iter1))  # e
print(next(iter1))  # k

"""


