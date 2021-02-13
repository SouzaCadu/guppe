import unittest

from atividades import comer, dormir, eh_engracada


class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """
        Testando a função
        :return:
        """
        self.assertEqual(
            comer("batata doce", True),
            "Estou comendo batata doce porque é saudável.")

    def test_comer_pizza(self):
        """
        Testando a função
        :return:
        """
        self.assertEqual(
            comer(comida="pizza", saudavel=False),
            "Estou comendo pizza porque só se vive uma vez.")

    def test_dormir_pouco(self):
        """
        Testando a função
        :return:
        """
        self.assertEqual(
            dormir(4),
            "Estou cansando, porque dormi pouco.")

    def test_dormir_muito(self):
        """
        Testando a função
        :return:
        """
        self.assertEqual(
            dormir(10),
            "Estou atraso para o trabalho, dormi demais.")


    def test_eh_engracada(self):
        # self.assertEqual(eh_engracada('Sérgio Malandro'), False)
        self.assertFalse(eh_engracada('Sérgio Malandro'))
        self.assertTrue(eh_engracada('Jim'), 'Jim deveria ser engraçado')


if __name__ == "__main__":
    unittest.main()