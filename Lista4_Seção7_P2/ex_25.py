"""
faça um programa para determinar a próxima jogada em jogo da velha
o tabuleiro é uma matriz 3 x 3
"""

from collections import Counter

print('Jogo da velha')


def linha_check(matriz, i):
    """Função para conferir o número de X/O na linha i de matriz.
       Retorna 1 se há 3 X's, -1 se há 3 O's, e 0 caso contrário."""
    if Counter(matriz[i]).get('X') == 3:
        return 1
    elif Counter(matriz[i]).get('O') == 3:
        return -1
    return 0


def coluna_check(matriz, j):
    """Função para conferir o número de X/O na coluna j de matriz.
           Retorna 1 se há 3 X's, -1 se há 3 O's, e 0 caso contrário."""
    m_trans = [[matriz[j][i] for j in range(3)] for i in range(3)]
    return linha_check(m_trans, j)


def diag_check(matriz):
    """Função para conferir o número de X/O na duas diagonais de matriz.
           Retorna 1 se há 3 X's, -1 se há 3 O's, e 0 caso contrário."""
    diag1 = [matriz[i][i] for i in range(3)]

    for linha in matriz:
        linha.reverse()

    diag2 = [matriz[i][i] for i in range(3)]

    if Counter(diag1).get('X') == 3 or Counter(diag2).get('O') == 3:
        return 1
    elif Counter(diag1).get('X') == 3 or Counter(diag2).get('O') == 3:
        return -1
    return 0


jogo = [[0 for _ in range(3)] for _ in range(3)]
for linha in jogo:
    print(linha)

jogada = 1
while True:
    if jogada % 2:
        print('Jogador 1 - Insira a posição')
    else:
        print('Jogador 2 - Insira a posição')

    jogada_check = True

    i = int(input('Linha (0 a 2): '))
    j = int(input('Coluna (0 a 2): '))

    if jogo[i][j] != 0:
        jogada_check = False

    while not jogada_check:
        print('Jogada inválida.')

        i = int(input('Linha (0 a 2): '))
        j = int(input('Coluna (0 a 2): '))

        if jogo[i][j] == 0:
            jogada_check = True

    if jogada % 2:
        jogo[i][j] = 'X'
    else:
        jogo[i][j] = 'O'

    for linha in jogo:
        print(linha)

    if linha_check(jogo, i) == 1 or coluna_check(jogo, j) == 1 or diag_check(jogo) == 1:
        print(f'Jogador 1 venceu! Número de jogadas: {jogada}')
        break
    elif linha_check(jogo, i) == -1 or coluna_check(jogo, j) == -1 or diag_check(jogo) == -1:
        print(f'Jogador 2 venceu! Número de jogadas: {jogada}')
        break
    else:
        jogada += 1

    if jogada > 9:
        print('Empate!')
        break