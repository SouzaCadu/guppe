"""
Módulo Collections - Default Dict

Com Default Dict, ao criar um dicionário, podemos informar um valor padrão de chave usando uma função lambda
evitando que o programa retorne um erro caso a chave não exista

"""

# Criando um dicionário

dicionario = {"instrutor": "Geek University", "curso": "Programação em Python Essencial"}
print(dicionario["instrutor"])
# print(dicionario["plataforma"]) - retorna uma KeyError

# Usando o defaultdict para evitar erros

from collections import defaultdict

dicionario1 = defaultdict(lambda: 0)
print(dicionario1["plataforma"])
print(dicionario1)
