"""
Antes e depois do hooks

Hooks são os testes em si.

setup() - é executado antes de cada método de teste, é útil para criarmos instâncias de objetos e outros
dados.

tearDown() - é executado ao final de cada metodo de teste. É útil para excluir dados ou fechar conexões
com bancos de dados.

"""

import unittest


class ModuloTest(unittest.TestCase):


    def setUp(self):
        #configurações do setup()
        pass

    def test_primeiro(self):
        # setup vai rodar antes do teste
        # tearDown vai rodar apos o teste
        pass

    def test_segundo(self):
        # setup vai rodar antes do teste
        # tearDown vai rodar apos o teste
        pass

    def tearDown(self) -> None:
        # configurações do tearDown()
        pass

