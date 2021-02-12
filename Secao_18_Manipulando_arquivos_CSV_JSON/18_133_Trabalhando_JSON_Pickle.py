"""
JSON e Pickle

JSON (Java Script Object Notation) são um tipo de arquivo muito utilizado em API's


"""

import json, jsonpickle

ret = json.dumps(["produto", {"Playstation 5": ("2TB", "Novo", "220v", 4750)}])

print(ret, type(ret))


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

maine_coon = Gato("Maynard", "Maine Coon")

print(maine_coon, maine_coon.__dict__)

ret2 = json.dumps(maine_coon.__dict__)

print(ret2)

ret3 = jsonpickle.encode(maine_coon)

print(ret3)

with open("gato.json", "w") as arquivo:
    ret4 = jsonpickle.encode(maine_coon)
    arquivo.write(ret4)

with open("gato.json", "r") as arquivo:
    conteudo = arquivo.read()
    ret5 = jsonpickle.decode(conteudo)
    print(ret5, type(ret5))
    print(ret5.nome, ret5.raca)

