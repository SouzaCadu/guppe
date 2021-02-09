"""
Listas aninhadas

São listas de listas, equivalem a arrays ou matrizes em outras linguagens

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

[[print(i) for i in lista] for lista in listas]

tabuleiro = [[numero for numero in range(1, 4)] for numero in range(1, 4)]
print(tabuleiro)

velha = [["X" if numero % 2 == 0 else "O" for numero in range(1, 4)] for numero in range(1, 4)]
print(velha)

"""

