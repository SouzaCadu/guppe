"""
Módulo Collections - Ordered Dict
"""
# Dicionários não garantem a ordenação

dict1 = {"a": 1, "c": 3, "b": 2, "f": 6, "e": 5, "d": 4}
for chave, valor in dict1.items():
    print(f"chave = {chave}: valor {valor}")

from collections import OrderedDict

dict2 = OrderedDict({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6})
for chave, valor in dict2.items():
    print(f"chave = {chave}: valor {valor}")
