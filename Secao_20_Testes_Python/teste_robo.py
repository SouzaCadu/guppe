import unittest

from robo import Robo


class RoboTestes(unittest.TestCase):

    def setUp(self) -> None:
        self.jarvis = Robo("Jarvis", bateria=50)

    def teste_carregar(self):
        self.jarvis.carregar()
        self.assertEqual(self.jarvis.bateria, 100)

    def teste_dizer_nome(self):
        self.assertEqual(self.jarvis.dizer_nome(), "Eu sou JARVIS !!!")
        self.assertEqual(self.jarvis.bateria, 49, "A bateria deveria estar em 49%")

    def tearDown(self) -> None:
        print("tearDown() sendo executado...")


if __name__ == "__main__":
    unittest.main()
