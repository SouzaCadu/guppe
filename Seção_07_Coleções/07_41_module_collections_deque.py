"""
Módulo Collections - Deque

Deque é uma lista de alta performance, aceita os mesmos métodos de uma lista
"""

from collections import deque

deq = deque("geek")
print(deq)

# Adicionando itens
deq.append("y")
print(deq)

deq.appendleft("o")  # adiciona o elemento no começo da lista
print(deq)

# Removendo elementos
deq.pop()  # remove e retorna o último elemento
print(deq)
deq.popleft()  # remove e retorna o primeiro elemento
print(deq)
